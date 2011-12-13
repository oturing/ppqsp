# coding: utf-8

"""
Exemplo de uma classe com propriedades

A classe ItemPedido deve ser instanciada com os dados essenciais que sao:
descricao do item, preco unitario e quantidade.

    >>> bolas = ItemPedido('bola de golf', 2, 10)
    >>> bolas.descr
    'bola de golf'
    >>> bolas.qtd
    10
	
O atributo qtd de um ItemPedido nunca pode ser < 1:

    >>> duendes = ItemPedido('duende verde', 2.99, 0)
    Traceback (most recent call last):
      ...
    TypeError: a quantidade deve ser >= 1
    >>> duendes = ItemPedido('duende verde', 2.99, 13)
    >>> duendes.qtd
    13
    >>> duendes.qtd = -1
    Traceback (most recent call last):
      ...
    TypeError: a quantidade deve ser >= 1
    >>> duendes.qtd = 20
    >>> duendes.qtd
    20


"""

class ItemPedido(object):
    """um item de um pedido"""
    def __init__(self, descr, pr_unitario, qtd):
        self.descr = descr
        self.pr_unitario = pr_unitario
        self.qtd = qtd

    @property
    def qtd(self):
        return self.__qtd

    @qtd.setter
    def qtd(self, qtd):
        if qtd < 1:
            raise TypeError('a quantidade deve ser >= 1')
        self.__qtd = qtd

