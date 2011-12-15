from time import time
from urllib2 import urlopen
import os
import shutil
from itertools import takewhile

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

with open('bandeiras.txt') as nomes:
    ateh_b = takewhile(lambda s: s[0] in 'ab', nomes)
    for index, nome in enumerate(ateh_b):
        nome = nome.strip()
        print index+1, nome
        img_orig = urlopen(BASE_URL+nome)
        with open(DESTINO+nome, 'wb') as img_local:
            img = img_orig.read()
            img_local.write(img)
            qt_bytes += len(img)
        img_orig.close()
	qt_baixar = index+1

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

"""

