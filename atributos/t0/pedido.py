#!/usr/bin/env python
# coding: utf-8

"""
Exemplo de uma classe com um propriedade::

    >>> bolas = ItemPedido('bolas de golfe', 5.00, 6)
    >>> bolas.preco_unit
    5.0
    >>> bolas.qtd
    6
    >>> bolas.total()
    30.0

Este exemplo ilustra a implementacao de uma propriedade usando
o decorator @property para evitar quantidades negativas::

    >>> duendes = ItemPedido('duende verde', 300, -1)
    Traceback (most recent call last):
      ...
    TypeError: quantidade deve ser > 0
    >>> duendes = ItemPedido('duende verde', 0, 10)
    Traceback (most recent call last):
      ...
    TypeError: preco_unit deve ser > 0

Queremos que seja proibido atribuir uma quantidade negativa a uma
instancia de ItemPedido existente::

    >>> lupas = ItemPedido('lente de aumento 3x', 3.99, 10)
    >>> lupas.qtd
    10
    >>> lupas.qtd = 12
    >>> lupas.qtd
    12
    >>> lupas.qtd = -10
    Traceback (most recent call last):
      ...
    TypeError: quantidade deve ser > 0


"""

class ItemPedido(object):
    """Representa um item de um pedido.

    Instancias desta classe formam as linhas de uma fatura.
    """
    def __init__(self, descr, preco_unit, qtd):
        self.descr = descr
        if preco_unit > 0:
            self.preco_unit = preco_unit
        else:
            raise TypeError('preco_unit deve ser > 0')
        self.qtd = qtd

    def total(self):
        return self.preco_unit * self.qtd

    @property
    def qtd(self):
        return self.__qtd

    @qtd.setter
    def qtd(self, valor):
        if valor > 0:
            self.__qtd = valor
        else:
            raise TypeError('quantidade deve ser > 0')
