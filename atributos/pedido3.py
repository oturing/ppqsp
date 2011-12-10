# coding: utf-8

"""
Exemplo de uma classe com descritores

A classe ItemPedido deve ser instanciada com os dados essenciais que sao:
descricao do item, preco unitario e quantidade.

    >>> bolas = ItemPedido('bola de golf', 2, 10)
    >>> bolas.descr
    'bola de golf'
    >>> bolas.qtd
    10
	
O atributo qtd de um ItemPedido nunca pode ser <= 0:

    >>> duendes = ItemPedido('duende verde', 2.99, 0)
    Traceback (most recent call last):
      ...
    TypeError: quantidade deve ser > 0
    >>> duendes = ItemPedido('duende verde', 2.99, 13)
    >>> duendes.qtd
    13
    >>> duendes.qtd = -1
    Traceback (most recent call last):
      ...
    TypeError: quantidade deve ser > 0
    >>> duendes.qtd = 20
    >>> duendes.qtd
    20

O preco também nao pode ser <= 0:

    >>> saci = ItemPedido('saci', -1, 0)
    Traceback (most recent call last):
      ...
    TypeError: quantidade deve ser > 0

"""
from descritores import Quantidade

class ItemPedido(object):
    """um item de um pedido"""

    qtd = Quantidade()
    pr_unitario = Quantidade()
    
    def __init__(self, descr, pr_unitario, qtd):
        self.descr = descr
        self.qtd = qtd
        self.pr_unitario = pr_unitario
