from time import time
from urllib2 import urlopen, URLError
import os
import shutil

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
qt_baixou = 0

with open('bandeiras.txt') as nomes:
    for index, nome in enumerate(s for s in nomes if s[0] == 'a'):
        nome = nome.strip()
        print index+1, nome
        try:
            img_orig = urlopen(BASE_URL+nome)
            with open(DESTINO+nome, 'wb') as img_local:
                img = img_orig.read()
                img_local.write(img)
                qt_bytes += len(img)
            img_orig.close()
        except URLError as exc:
            print exc
            continue
                
    qt_baixou += 1

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

"""

