# coding: utf-8

from tornado import httpclient, ioloop

from utilflags import ler_siglas, salvar, reportar, BASE_URL

qt_bytes = 0
qt_arqs = 0
conj_baixar = set()

def processar(response):
    global qt_bytes, qt_arqs
    nome = response.request.url[len(BASE_URL):]
    if response.error:
        print "Error:", response.error
        print '  Tentando de novo...'
        print response.request.url
        http_client.fetch(response.request.url, handle_request)
    else:
        qt_bytes += salvar(nome, response.body)
        qt_arqs += 1
        print '\t\t\t', nome, '--> salvo'
        conj_baixar.discard(nome)
        if not conj_baixar:
            ioloop.IOLoop.instance().stop()

def baixar(qtd):
    """ busca a quantidade ``qtd`` de bandeiras """

    http_client = httpclient.AsyncHTTPClient()

    for num, sigla in enumerate(ler_siglas(qtd), 1):
        nome = sigla + '-lgflag.gif'
        print '\t%3d\t%s' % (num, nome)
        url = BASE_URL+nome
        conj_baixar.add(nome)
        http_client.fetch(url, processar)

    ioloop.IOLoop.instance().start()
    return qt_bytes, qt_arqs

if __name__=='__main__':
    reportar(baixar)


"""
$ python sincrono.py 10
baixando 10 arquivos...
      1 aa-lgflag.gif
      2 ac-lgflag.gif
      3 ae-lgflag.gif
      ...
96442 bytes baixados em 10 arquivos
tempo transcorrido: 8.83s
(tornado.env)lontra:async luciano$ python assincrono.py 10
baixando 10 arquivos...
      1 aa-lgflag.gif
      2 ac-lgflag.gif
      3 ae-lgflag.gif
      ...
            ac-lgflag.gif --> salvo
            ae-lgflag.gif --> salvo
            aa-lgflag.gif --> salvo
            ...
96442 bytes baixados em 10 arquivos
tempo transcorrido: 1.23s
"""

