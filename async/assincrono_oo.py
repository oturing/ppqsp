# coding: utf-8

from tornado import httpclient, ioloop

from utilflags import ler_siglas, salvar, reportar, BASE_URL

class Processador(object):
    qt_bytes = 0
    qt_arqs = 0
    conj_baixar = set()

    def __init__(self, nome, numero):
        Processador.conj_baixar.add(nome)
        self.nome = nome
        self.numero = numero

    def processar(self, response):
        if response.error:
            print 'Erro: ', response.error
            print '\tTentando de novo...', response.request.url
            http_client.fetch(response.request.url, self.processar)
        else:
            Processador.qt_bytes += salvar(self.nome, response.body)
            Processador.qt_arqs += 1
            print '\t\t\t%3d\t%s --> salvo' % (self.numero, self.nome)
            Processador.conj_baixar.discard(self.nome)
            if not Processador.conj_baixar:
                ioloop.IOLoop.instance().stop()

def baixar(qtd):
    """ busca a quantidade ``qtd`` de bandeiras """

    http_client = httpclient.AsyncHTTPClient()

    for num, sigla in enumerate(ler_siglas(qtd), 1):
        nome = sigla + '-lgflag.gif'
        print '\t%3d\t%s' % (num, nome)
        url = BASE_URL+nome
        proc = Processador(nome, num)
        http_client.fetch(url, proc.processar)

    ioloop.IOLoop.instance().start()
    return Processador.qt_bytes, Processador.qt_arqs

if __name__=='__main__':
    reportar(baixar)


