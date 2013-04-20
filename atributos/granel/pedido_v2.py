# coding: utf-8

"""

    >>> passa = ItemPedido('uva passa', .5, 7.)
    >>> passa.preco
    7.0
    >>> passa.subtotal()
    3.5
    >>> passa.peso = 10
    >>> passa.peso
    10
    >>> passa.subtotal()
    70.0
    >>> passa.peso = -1
    Traceback (most recent call last):
      ...
    ValueError: valor deve ser > 0
    >>> passa.__peso  # violação de encapsulamento???
    Traceback (most recent call last):
      ...
    AttributeError: 'ItemPedido' object has no attribute '__peso'

"""


class ItemPedido(object):

    def __init__(self, descricao, peso, preco):
        self.descricao = descricao
        self.peso = peso
        self.preco = preco

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        if valor > 0:
            self.__peso = valor
        else:
            raise ValueError('valor deve ser > 0')

    def subtotal(self):
        return self.peso * self.preco
