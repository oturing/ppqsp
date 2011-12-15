from time import time
from urllib2 import urlopen
import os
import shutil
from itertools import takewhile
from tornado import httpclient, ioloop

BASE_URL = ('https://www.cia.gov/library/publications/the-world-factbook'
            '/graphics/flags/large/')

DESTINO = './bandeiras/'

try:
    shutil.rmtree(DESTINO)
except OSError:
    pass

os.mkdir(DESTINO)

t0 = time()
baixar = set()
qt_bytes = 0
qt_baixar = 0

def handle_request(response):
    global qt_bytes
    if response.error:
        print "Error:", response.error
    else:
        nome = response.request.url.replace(BASE_URL, '')
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
        print index+1, nome
        baixar.add(nome)
        http_client.fetch(BASE_URL+nome, handle_request)
    qt_baixar = len(baixar)

ioloop.IOLoop.instance().start()

print qt_bytes, 'bytes baixados em %s arquivos' % qt_baixar
print 'tempo transcorrido:', time()-t0

"""
sincrono.py:
    ...
    29 bc-lgflag.gif
    30 bv-lgflag.gif
    31 br-lgflag.gif
    228410 bytes baixados em 31 arquivos
    tempo transcorrido: 43.5865662098

assincrono.py:
    ...
    29 bc-lgflag.gif
    30 bv-lgflag.gif
    31 br-lgflag.gif
    228410 bytes baixados em 31 arquivos
    tempo transcorrido: 8.02110886574
"""

