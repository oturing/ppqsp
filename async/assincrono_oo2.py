from time import time
from urllib2 import urlopen
import os
import shutil
from itertools import takewhile
from tornado import httpclient, ioloop

BASE_URL = ('https://www.cia.gov/library/publications/the-world-factbook'
            '/graphics/flags/large/')

DESTINO = './bandeiras/'

#try:
#    shutil.rmtree(DESTINO)
#except OSError:
#    pass

#os.mkdir(DESTINO)

t0 = time()
qt_bytes = 0
qt_baixou = 0
baixar = {}


class Salvador(object):
    def __init__(self, nome, index):
        self.nome = nome
        self.index = index
        
    def salvar(self, response):
        global qt_bytes, qt_baixou
        nome = self.nome
        index = self.index
        #nome = response.request.url[len(BASE_URL):]
        if response.error:
            print "\t*** Erro ao baixar", nome
            pass
        else:
            with open(DESTINO+nome, 'wb') as img_local:
                img_local.write(response.body)
            print '\t-->', index, nome
            qt_bytes += len(response.body)
            qt_baixou += 1
        del baixar[nome]
        if not baixar:
            ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()

with open('bandeiras.txt') as nomes:
    ateh_b = takewhile(lambda s: s[0] in 'a', nomes)
    for index, nome in enumerate(ateh_b):
        nome = nome.strip()
        print index+1, nome
        baixar[nome] = index+1
        salvador = Salvador(nome, index)
        http_client.fetch(BASE_URL+nome, salvador.salvar)

ioloop.IOLoop.instance().start()

print qt_bytes, 'bytes baixados em %s arquivos' % qt_baixou
print 'tempo transcorrido:', time()-t0

"""
sincrono.py:
    ...
    36 bv-lgflag.gif
    37 bx-lgflag.gif
    38 by-lgflag.gif
    262865 bytes baixados em 38 arquivos
    tempo transcorrido: 41.6797399521

assincrono.py:
    ...
    36 bv-lgflag.gif
    37 bx-lgflag.gif
    38 by-lgflag.gif
    262865 bytes baixados em 38 arquivos
    tempo transcorrido: 5.27639985085
"""

