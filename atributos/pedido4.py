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
    TypeError: qtd deve ser > 0
    >>> duendes = ItemPedido('duende verde', 2.99, 13)
    >>> duendes.qtd
    13
    >>> duendes.qtd = -1
    Traceback (most recent call last):
      ...
    TypeError: qtd deve ser > 0
    >>> duendes.qtd = 20
    >>> duendes.qtd
    20

O preco também nao pode ser <= 0:

    >>> saci = ItemPedido('saci', -1, 10)
    Traceback (most recent call last):
      ...
    TypeError: pr_unitario deve ser > 0

"""
class Quantidade(object):
    def __set__(self, instance, valor):
        if not hasattr(self, 'nome_atr'):
            for nome, atr in instance.__class__.__dict__.items():
                if atr is self:
                    self.nome_atr = '__'+nome
                    break
            else: # only if the for loop terminates without break
                assert False, 'descriptor not found in class'
        if valor < 1:
            raise TypeError('%s deve ser > 0' % self.nome_atr[2:])
        setattr(instance, self.nome_atr, valor)

    def __get__(self, instance, owner):
        return getattr(instance, self.nome_atr)

class ItemPedido(object):
    """um item de um pedido"""

    qtd = Quantidade()
    pr_unitario = Quantidade()

    def __init__(self, descr, pr_unitario, qtd):
        self.descr = descr
        self.qtd = qtd
        self.pr_unitario = pr_unitario
