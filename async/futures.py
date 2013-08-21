# coding: utf-8

import contextlib
import urllib2
import concurrent.futures # usando backport https://pypi.python.org/pypi/futures

from utilflags import ler_siglas, salvar, reportar, BASE_URL


def baixar_uma(nome):
    url = BASE_URL+nome
    with contextlib.closing(urllib2.urlopen(url)) as img_orig:
        return img_orig.read()

def baixar(qtd):
    """ busca e salva a quantidade ``qtd`` de bandeiras """

    qt_bytes = 0
    qt_arqs = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

        pendentes = {}
        for (numero, sigla) in enumerate(ler_siglas(qtd), 1):
            nome = sigla + '-lgflag.gif'
            pendentes[executor.submit(baixar_uma, nome)] = numero, nome
            print '\t%3d\t%s' % (numero, nome)

        for future in concurrent.futures.as_completed(pendentes):
            numero, nome = pendentes[future]
            try:
                bytes = future.result()
            except Exception as exc:
                print('gerou erro ao baixar %s (#%s): %s' % (nome, numero, exc))
            else:
                qt_bytes += salvar(nome, bytes)
                qt_arqs += 1
                print '\t\t\t%3d\t%s --> salvo' % (numero, nome)

    return qt_bytes, qt_arqs

if __name__=='__main__':
    reportar(baixar)

"""
$ python sincrono_queue.py 3
baixando 3 arquivos...
      1 aa-lgflag.gif
      2 ac-lgflag.gif
      3 ae-lgflag.gif
              2 ac-lgflag.gif --> salvo
              1 aa-lgflag.gif --> salvo
              3 ae-lgflag.gif --> salvo
11889 bytes baixados em 3 arquivos
tempo transcorrido: 0.93s

"""
