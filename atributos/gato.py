# coding: utf-8


"""
Registro de gato em um Pet Shop::

    >>> felix = Gato('Felix')
    >>> felix.nome
    'Felix'
    >>> felix.idade
    0
    >>> print felix
    Felix (0)

Note: até aqui, ``idade`` é um atributo da classe ``Gato``::

    >>> Gato.idade
    0

Agora vamos atribuir uma ``idade`` a Felix::

    >>> felix.idade = 5
    >>> print felix
    Felix (5)

Isso não muda a ``idade`` da classe::

    >>> Gato.idade
    0


"""

class Gato(object):

    idade = 0

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return '%s (%s)' % (self.nome, self.idade)
