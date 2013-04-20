# coding: utf-8

import contextlib
import urllib2

from utilflags import ler_siglas, salvar, reportar, BASE_URL

def baixar(qtd):
    """ busca e salva a quantidade ``qtd`` de bandeiras """
    qt_bytes = 0
    qt_arqs = 0

    for num, sigla in enumerate(ler_siglas(qtd), 1):
        # baixar bandeiras com inicial 'a' ou 'b'
        nome = sigla + '-lgflag.gif'
        print '\t%3d\t%s' % (num, nome)
        url = BASE_URL+nome
        with contextlib.closing(urllib2.urlopen(url)) as img_orig:
            img = img_orig.read()
            qt_bytes += salvar(nome, img)
            qt_arqs += 1

    return qt_bytes, qt_arqs

if __name__=='__main__':
    reportar(baixar)

"""
$ python sincrono.py 3
baixando 3 arquivos...
      1 aa-lgflag.gif
      2 ac-lgflag.gif
      3 ae-lgflag.gif
11889 bytes baixados em 3 arquivos
tempo transcorrido: 12.62s

"""
