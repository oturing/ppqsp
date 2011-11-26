'''
    >>> from baralho import Baralho
    >>> b = Baralho()
    >>> b[0]
    <A de copas>
    >>> b[:3]
    [<A de copas>, <2 de copas>, <3 de copas>]
    >>> b[-3:]
    [<J de paus>, <Q de paus>, <K de paus>]
    >>> for carta in b:                             # doctest:+ELLIPSIS
    ...     print carta
    <A de copas>
    <2 de copas>
    <3 de copas>
    <4 de copas>
    <5 de copas>
    ...
    >>> for carta in reversed(b):                   # doctest:+ELLIPSIS
    ...     print carta
    <K de paus>
    <Q de paus>
    <J de paus>
    <10 de paus>
    ...
    >>>

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

    def __getitem__(self, pos):
        return self.cartas[pos]

    def __len__(self):
        return len(self.cartas)
