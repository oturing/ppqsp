# coding: utf-8

"""

    >>> passa = ItemPedido('uva passa', .5, 7.)
    >>> passa.preco
    7.0
    >>> passa.subtotal()
    3.5
    >>> passa.peso = -1   # problema!!!
    >>> passa.subtotal()  # agora o comerciante deve R$7 para o freguês...
    -7.0


"""



class ItemPedido(object):

    def __init__(self, descricao, peso, preco):
        self.descricao = descricao
        self.peso = peso
        self.preco = preco

    def subtotal(self):
        return self.peso * self.preco
