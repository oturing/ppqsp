# coding: utf-8

"""
Exemplo de uma classe com propriedades

A classe ItemPedido deve ser instanciada com os dados
essenciais que sao: descricao do item, quantidade e 
preco unitario.

    >>> bolas = ItemPedido('bola de golf', 10, 2)
    >>> bolas.descr
    'bola de golf'
    >>> bolas.qtd
    10
	
O atributo qtd de um ItemPedido nunca pode ser < 1:

    >>> duendes = ItemPedido('duende verde', 0, 2.99)
    Traceback (most recent call last):
      ...
    TypeError: quantidade deve ser > 0
    >>> duendes = ItemPedido('duende verde', 13, 2.99)
    >>> duendes.qtd
    13
    >>> duendes.qtd = -1
    Traceback (most recent call last):
      ...
    TypeError: quantidade deve ser > 0
    >>> duendes.qtd = 20
    >>> duendes.qtd
    20

Se o argumento qtd for None, eh usado um valor default, definido
na classe:

    >>> unicornio = ItemPedido('unicornio', None, 199000)
    >>> unicornio.qtd
    1

"""

class Quantidade(object):
    def __init__(self, nome_atr):
        self.nome_atr = nome_atr
    def __set__(self, instance, valor):
        if valor < 1:
            raise TypeError('quantidade deve ser > 0')
        else:
            setattr(instance, '__'+self.nome_atr, valor)
    def __get__(self, instance, owner):
        nome_atr_real = '__'+self.nome_atr
        if hasattr(instance, nome_atr_real):
            return getattr(instance, nome_atr_real)
        else:
            return getattr(owner, self.nome_atr+'_default')  


class ItemPedido(object):
    """um item de um pedido"""

    qtd = Quantidade('qtd')
    qtd_default = 1

    def __init__(self, descr, qtd, pr_unitario):
        self.descr = descr
        if qtd is not None:
            self.qtd = qtd
        self.pr_unitario = pr_unitario
