# coding: utf-8

from tornado import httpclient, ioloop, gen

from utilflags import ler_siglas, salvar, reportar, BASE_URL

qt_bytes = 0
qt_arqs = 0
conj_baixar = set()

@gen.engine
def processar(cliente, nome, numero):
    global qt_bytes, qt_arqs
    print '\t%3d\t%s' % (numero, nome)
    conj_baixar.add(nome)
    url = BASE_URL+nome
    response = yield gen.Task(cliente.fetch, url)
    if response.error:
        print 'Erro: ', response.error
        print '\tTentando de novo...', response.request.url
        http_client.fetch(response.request.url, handle_request)
    else:
        qt_bytes += salvar(nome, response.body)
        qt_arqs += 1
        print '\t\t\t%3d\t%s --> salvo' % (numero, nome)
        conj_baixar.discard(nome)
        if not conj_baixar:
            ioloop.IOLoop.instance().stop()

def baixar(qtd):
    """ busca a quantidade ``qtd`` de bandeiras """

    cliente = httpclient.AsyncHTTPClient()

    for num, sigla in enumerate(ler_siglas(qtd), 1):
        nome = sigla + '-lgflag.gif'
        processar(cliente, nome, num)

    ioloop.IOLoop.instance().start()
    return qt_bytes, qt_arqs

if __name__=='__main__':
    reportar(baixar)
