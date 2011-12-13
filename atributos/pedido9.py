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


Podemos obter a lista dos descritores de ItemPedido, na ordem em que
foram declarados em ItemPedido:

    >>> ItemPedido.listar_descritores()
             qtd : Quantidade
           descr : Palavras
     pr_unitario : Quantidade


"""

from abc import ABCMeta, abstractmethod
from operator import attrgetter

class OrderedDescriptor(object):

    __instance_counter = 0

    def __new__(cls, *args):
        new_instance = object.__new__(cls)
        new_instance._instance_index = OrderedDescriptor.__instance_counter
        OrderedDescriptor.__instance_counter += 1
        return new_instance

class ValidatedDescriptor(OrderedDescriptor):
    __metaclass__ = ABCMeta

    @abstractmethod
    def validator(self, instance, value):
        """Return value or raise TypeError for invalid values

        This method is invoked by the __set__ method of the descriptor.
        Parameters are the same for __set__: self, instance, value.
        """

    def __set__(self, instance, value): # template method pattern
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

class OrderedModelMeta(type):
    def __new__(cls, name, bases, dict):
        ordered_descriptors = []
        for name, attr in dict.items():
            if isinstance(attr, OrderedDescriptor):
                ordered_descriptors.append(attr)
                attr.attr_name = name
        ordered_descriptors.sort(key=attrgetter('_instance_index'))
        dict['_ordered_descriptors'] = ordered_descriptors
        return type.__new__(cls, name, bases, dict)

class OrderedModel(object):
    __metaclass__ = OrderedModelMeta

    @classmethod
    def list_ordered_descriptors(cls):
        return cls._ordered_descriptors

class ItemPedido(OrderedModel):
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
        for atr in cls.list_ordered_descriptors():
            print '%12s : %s' % (atr.attr_name, atr.__class__.__name__)

