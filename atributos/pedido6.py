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

    >>> saci = ItemPedido('saci perere', -1, 10)
    Traceback (most recent call last):
      ...
    TypeError: pr_unitario deve ser > 0


E a descricao deve ter pelo menos duas palavras:

    >>> saci = ItemPedido('saci', -1, 10)
    Traceback (most recent call last):
      ...
    TypeError: descr deve ter pelo menos 2 palavras


Podemos obter a lista dos descritores de ItemPedido:

    >>> ItemPedido.listar_descritores()
           descr : Palavras
     pr_unitario : Quantidade
             qtd : Quantidade

Mas os descritores não aparecem na ordem em que foram declarados.

"""

from abc import ABCMeta, abstractmethod

class ValidatedDescriptor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def validator(self, instance, value):
        """Return value or raise TypeError for invalid values

        This method is invoked by the __set__ method of the descriptor.
        Parameters are the same for __set__: self, instance, value.
        """

    def __set__(self, instance, value):
        if not hasattr(self, 'attr_name'):
            for name, attr in instance.__class__.__dict__.items():
                if attr is self:
                    self.attr_name = name
                    break
            else: # only if the for loop terminates without break
                assert False, 'descriptor not found in class'
        value = self.validator(instance, value)
        setattr(instance, '__'+self.attr_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, '__'+self.attr_name)


class Quantidade(ValidatedDescriptor):
    def validator(self, instance, value):
        value = int(value)
        if value < 1:
            raise TypeError('%s deve ser > 0' % self.attr_name)
        return value

class Palavras(ValidatedDescriptor):
    def __init__(self, min_palavras):
        self.min_palavras = min_palavras

    def validator(self, instance, value):
        if len(value.split()) < self.min_palavras:
            msg = '%s deve ter pelo menos %s palavras'
            raise TypeError(msg % (self.attr_name, self.min_palavras))
        return value


class ItemPedido(object):
    """um item de um pedido"""

    qtd = Quantidade()
    descr = Palavras(2)
    pr_unitario = Quantidade()

    def __init__(self, descr, pr_unitario, qtd):
        self.descr = descr
        self.qtd = qtd
        self.pr_unitario = pr_unitario

    @classmethod
    def listar_descritores(cls):
        for nome, atr in cls.__dict__.items():
            if isinstance(atr, ValidatedDescriptor):
                print '%12s : %s' % (nome, atr.__class__.__name__)

