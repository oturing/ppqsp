# coding: utf-8

import contextlib
import urllib2
import threading
from Queue import Queue

from utilflags import ler_siglas, salvar, reportar, BASE_URL

qt_bytes = 0
qt_arqs = 0
fila = Queue()

def baixar_uma(nome, numero):
    global qt_bytes, qt_arqs
    url = BASE_URL+nome
    with contextlib.closing(urllib2.urlopen(url)) as img_orig:
        img = img_orig.read()
        qt_bytes += salvar(nome, img)
        qt_arqs += 1
        print '\t\t\t%3d\t%s --> salvo' % (numero, nome)

NUM_THREADS = 100

def worker():
    while True:
        nome, numero = fila.get()
        baixar_uma(nome, numero)
        fila.task_done()

def baixar(qtd):
    """ busca e salva a quantidade ``qtd`` de bandeiras """

    # criar threads
    for i in range(NUM_THREADS):
        tarefa = threading.Thread(target=worker)
        tarefa.daemon = True
        tarefa.start()

    # enfileirar tarefas
    for numero, sigla in enumerate(ler_siglas(qtd), 1):
        # baixar bandeiras com inicial 'a' ou 'b'
        nome = sigla + '-lgflag.gif'
        print '\t%3d\t%s' % (numero, nome)
        fila.put((nome, numero))

    fila.join()

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
