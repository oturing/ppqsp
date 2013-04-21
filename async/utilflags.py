# coding: utf-8

import time
import os
import shutil
import sys

# URL onde ficam as bandeiras originais

BASE_URL = ('https://www.cia.gov/library/publications/'
            'the-world-factbook/graphics/flags/large/')

# Apache Local em lontra (Mac OS X)
#BASE_URL = 'http://localhost/~luciano/cia/flags/CIA_Flags_of_the_World_files/'

# $ cd ~/prj/oturing/ppqsp/async/flags/CIA_Flags_of_the_World_files
# $ python -m SimpleHTTPServer 8000
#BASE_URL = 'http://localhost:8000/'

DIR_DESTINO = './bandeiras/' # onde serão salvas as bandeiras

ARQ_SIGLAS = 'siglas.txt' # arquivo que contem as siglas dos paises

def recriar_diretorio():
    """ apaga e recria diretório de destino """
    try:
        shutil.rmtree(DIR_DESTINO)
    except OSError:
        pass
    os.mkdir(DIR_DESTINO)

def ler_siglas(qtd_max=None):
    """ lê siglas de bandeiras do arquivo, devolve lista """
    with open(ARQ_SIGLAS) as arq:
        siglas = arq.read().split()
    return siglas if qtd_max is None else siglas[:qtd_max]

def salvar(nome, carga):
    """ salva o arquivo remoto localmente, devolve numero de bytes salvos """
    with open(DIR_DESTINO+nome, 'wb') as arq_local:
        arq_local.write(carga)
    return len(carga)

def reportar(funcao_baixar):
    if len(sys.argv) == 2:
        qt_baixar = int(sys.argv[1])
    else:
        qt_baixar = 10
    recriar_diretorio()
    print 'baixando %s arquivos...' % qt_baixar
    t0 = time.time()
    qt_bytes, qt_arqs = funcao_baixar(qt_baixar)
    print qt_bytes, 'bytes baixados em %s arquivos' % qt_arqs
    print 'tempo transcorrido: %0.2fs' % (time.time()-t0)
