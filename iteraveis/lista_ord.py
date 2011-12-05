# coding: utf-8

'''
Testes de `__contains__` mixin de `Sequence`
(faz busca linear via `__getitem__`)::

    >>> lo = ListaOrdenada([3,2,1])
    >>> 1 in lo, 2 in lo, 3 in lo
    (True, True, True)
    >>> 0 in lo, 4 in lo
    (False, False)
    >>> lo = ListaOrdenada([3,2,4,1])
    >>> 1 in lo, 2 in lo, 3 in lo, 4 in lo
    (True, True, True, True)
    >>> 0 in lo, 5 in lo
    (False, False)
    >>> lo = ListaOrdenada([7])
    >>> 6 in lo, 7 in lo, 8 in lo
    (False, True, False)
    >>> lo = ListaOrdenada([])
    >>> 0 in lo
    False

Testes de `add`::

    >>> lo = ListaOrdenada([])
    >>> lo.add(3); list(lo)
    [3]
    >>> lo.add(5); list(lo) # doctest: +SKIP
    [3, 5]
    >>> lo.add(4); list(lo) # doctest: +SKIP
    [3, 4, 5]
    >>> lo.add(2); list(lo) # doctest: +SKIP
    [2, 3, 4, 5]
    >>> lo.add(3); list(lo) # doctest: +SKIP
    [2, 3, 3, 4, 5]

'''

from collections import Sequence

class ListaOrdenada(Sequence):
    def __init__(self, iteravel):
        self.__lista = list(sorted(iteravel))

    def __getitem__(self, index):
        return self.__lista[index]

    def __len__(self):
        return len(self.__lista)

    def add(self, novo):
        """Insere um item na lista ordenada, mantendo a ordem."""
        raise NotImplementedError('Exercício: implementar este médodo')

def desempenho():
    from timeit import repeat
    from pprint import pprint
    tam = 10**5
    expr = '''0 in l, %d in l, %d in l''' % (tam/2, tam)
    prep = '\n'.join([
        '''from __main__ import ListaOrdenada''',
        '''l = ListaOrdenada(range(%d))''' % tam])
    res = repeat(expr, prep, number=10)
    print(min(res))

def teste():
    import doctest
    return doctest.testmod()[0] # devolver falhas

if __name__=='__main__':
    falhas = teste()
    if not falhas:
        desempenho()
