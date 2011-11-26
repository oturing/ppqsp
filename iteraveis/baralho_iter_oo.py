'''
    >>> b = Baralho()
    >>> for carta in b:                             # doctest:+ELLIPSIS
    ...     print carta
    <A de copas>
    <2 de copas>
    <3 de copas>
    <4 de copas>
    <5 de copas>
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

    def __init__(self):
        self.cartas = [Carta(v, n)
                        for n in self.naipes
                        for v in self.valores]

    def __len__(self):
        return len(self.cartas)

    def __iter__(self):
        return IteradorBaralho(self)

class IteradorBaralho(object):
    def __init__(self, baralho):
        self.index = 0
        self.baralho = baralho
    def next(self):
        if self.index == len(self.baralho):
            raise StopIteration()
        # o iterador conhece a implementacao do Baralho
        res = self.baralho.cartas[self.index]
        self.index += 1
        return res
    def __iter__(self):
        return self