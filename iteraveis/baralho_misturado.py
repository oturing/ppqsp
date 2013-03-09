'''
    >>> def inverte(l):
    ...     l.reverse()
    >>> b = Baralho(inverte)
    >>> for carta in b:                             # doctest:+ELLIPSIS
    ...     print carta
    <K de paus>
    <Q de paus>
    <J de paus>
    <10 de paus>
    <9 de paus>
    ...

'''

from random import shuffle

class Carta(object):
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)

class Baralho(object):
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self, embaralhador=shuffle):
        self.embaralhador = embaralhador
        self.cartas = [Carta(v, n)
                        for n in self.naipes
                        for v in self.valores]

    def __len__(self):
        return len(self.cartas)

    def __iter__(self):
        indice = range(len(self.cartas))
        self.embaralhador(indice)
        for i in indice:
            yield self.cartas[i]






