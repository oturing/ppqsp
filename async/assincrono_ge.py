from time import time
from urllib2 import urlopen
import os
import shutil
from itertools import takewhile
from tornado import httpclient, ioloop, gen

BASE_URL = ('https://www.cia.gov/library/publications/the-world-factbook'
            '/graphics/flags/large/')

DESTINO = './bandeiras/'

try:
    shutil.rmtree(DESTINO)
except OSError:
    pass

os.mkdir(DESTINO)

t0 = time()
qt_bytes = 0
qt_baixar = 0
baixar = set()

@gen.engine
def buscar(index, nome):
    global qt_bytes
    baixar.add(nome)
    response = yield gen.Task(http_client.fetch, BASE_URL+nome)
    if response.error:
        print "Error:", response.error
    else:
        # nao precisamos mais redescobrir o nome do arquivo pois
        # continuamos na mesma funcao, nao perdemos o contexto
        # nome = response.request.url[len(BASE_URL):]
        print index+1, nome
        with open(DESTINO+nome, 'wb') as img_local:
            img_local.write(response.body)
        qt_bytes += len(response.body)
        baixar.remove(nome)
        if not baixar:
            ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()

with open('bandeiras.txt') as nomes:
    ateh_b = takewhile(lambda s: s[0] in 'ab', nomes)
    for index, nome in enumerate(ateh_b):
        nome = nome.strip()
        buscar(index, nome)
    qt_baixar = len(baixar)

ioloop.IOLoop.instance().start()

print qt_bytes, 'bytes baixados em %s arquivos' % qt_baixar
print 'tempo transcorrido:', time()-t0

"""
sincrono.py:
    ...
    36 bv-lgflag.gif
    37 bx-lgflag.gif
    38 by-lgflag.gif
    262865 bytes baixados em 38 arquivos
    tempo transcorrido: 41.6797399521

assincrono_ge.py:
    ...
    37 bx-lgflag.gif
    33 br-lgflag.gif
    34 bt-lgflag.gif
    262865 bytes baixados em 38 arquivos
    tempo transcorrido: 5.30196714401
"""

