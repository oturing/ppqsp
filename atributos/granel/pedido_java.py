# coding: utf-8

"""

    >>> passa = ItemPedido('uva passa', .5, 7.)
    >>> passa.preco
    7.0
    >>> passa.subtotal()
    3.5
    >>> passa.set_peso(10)
    >>> passa.get_peso()
    10
    >>> passa.subtotal()
    70.0
    >>> passa.set_peso(-1)
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
        self.set_peso(peso)
        self.preco = preco

    def get_peso(self):
        return self.__peso

    def set_peso(self, valor):
        if valor > 0:
            self.__peso = valor
        else:
            raise ValueError('valor deve ser > 0')

    def subtotal(self):
        return self.get_peso() * self.preco
