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
    TypeError: qtd deve ser > 0
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
    TypeError: qtd deve ser > 0


"""

class Quantidade(object):
    def __get__(self, instance, owner):
        return getattr(instance, '__'+self.nome_atr)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, '__'+self.nome_atr, value)
        else:
            raise TypeError('%s deve ser > 0' % self.nome_atr)

class ItemPedido(object):
    """Representa um item de um pedido.

    Instancias desta classe formam as linhas de uma fatura.
    """

    qtd = Quantidade()
    preco_unit = Quantidade()

    def nomear_descritores(self, cls):
        for nome, valor in cls.__dict__.items():
            if isinstance(valor, Quantidade):
                valor.nome_atr = nome

    def __init__(self, descr, preco_unit, qtd):
        self.nomear_descritores(self.__class__)
        self.descr = descr
        self.preco_unit = preco_unit
        self.qtd = qtd
        
    def total(self):
        return self.preco_unit * self.qtd

if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
