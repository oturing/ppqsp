from time import time
from urllib2 import urlopen
import os
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
baixar = {}

def salvar(response):
    global qt_bytes, qt_baixou
    nome = response.request.url[len(BASE_URL):]
    if response.error:
        print "Error:", response.error
        print '  Tentando de novo...'
        print response.request.url
        http_client.fetch(response.request.url, handle_request)
    else:
        with open(DESTINO+nome, 'wb') as img_local:
            img_local.write(response.body)
        qt_bytes = qt_bytes + len(response.body)
        baixar.pop(nome)
        print '-->', nome
        if not baixar:
            ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()

ULTIMO = 38

with open('bandeiras.txt') as nomes:
    for num, nome in enumerate(nomes, 1):
        nome = nome.strip()
        print num, nome
        baixar[nome] = num
        http_client.fetch(BASE_URL+nome, salvar)
        if num == ULTIMO:
            break

print '*' * 40, 'FIM DO LOOP DE REQUICOES'

ioloop.IOLoop.instance().start()

print qt_bytes, 'bytes baixados em %s arquivos' % num
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

