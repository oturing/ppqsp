'''
    >>> o = C(7)
    >>> o.x
    7
    >>> o._qtd_x
    7
    >>> o.x = -1
    Traceback (most recent call last):
      ...
    TypeError: quantidade < 0
    >>> o.x
    7

'''

class Quantidade(object):
    def __init__(self, nome_atr):
        self.nome_atr = nome_atr
    def __get__(self, instance, owner):
        return getattr(instance, '_qtd_'+self.nome_atr)
    def __set__(self, instance, value):
        value = int(value)
        if value >= 0:
            setattr(instance, '_qtd_'+self.nome_atr, value)
        else:
            raise TypeError('quantidade < 0')

class C(object):
    def __init__(self, x):
        self.x = x
    x = Quantidade('x')
