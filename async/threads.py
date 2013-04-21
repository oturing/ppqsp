# coding: utf-8

import contextlib
import urllib2
import threading

from utilflags import ler_siglas, salvar, reportar, BASE_URL

qt_bytes = 0
qt_arqs = 0
conj_baixar = set()

def baixar_uma(nome, numero):
    global qt_bytes, qt_arqs
    url = BASE_URL+nome
    with contextlib.closing(urllib2.urlopen(url)) as img_orig:
        img = img_orig.read()
        qt_bytes += salvar(nome, img)
        qt_arqs += 1
        print '\t\t\t%3d\t%s --> salvo' % (numero, nome)
        conj_baixar.discard(nome)

# GNU/Linux e Mac OSX suportam poucas centenas de threads
MAX_THREADS = 100

def baixar(qtd):
    """ busca e salva a quantidade ``qtd`` de bandeiras """

    assert qtd <= MAX_THREADS, 'limite: %s downloads paralelos' % MAX_THREADS
    for num, sigla in enumerate(ler_siglas(qtd), 1):
        # baixar bandeiras com inicial 'a' ou 'b'
        nome = sigla + '-lgflag.gif'
        print '\t%3d\t%s' % (num, nome)
        tarefa = threading.Thread(target=baixar_uma, args=(nome, num))
        tarefa.start()
        conj_baixar.add(nome)

    while conj_baixar:
        pass

    return qt_bytes, qt_arqs

if __name__=='__main__':
    reportar(baixar)

"""
$ python sincrono_threads.py 3
baixando 3 arquivos...
      1 aa-lgflag.gif
      2 ac-lgflag.gif
      3 ae-lgflag.gif
              1 aa-lgflag.gif --> salvo
              2 ac-lgflag.gif --> salvo
              3 ae-lgflag.gif --> salvo
11889 bytes baixados em 3 arquivos
tempo transcorrido: 1.08s
"""
