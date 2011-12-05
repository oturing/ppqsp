'''
    >>> o = C(7)
    >>> o.x
    7
    >>> o.x = 8
    Traceback (most recent call last):
      ...
    AttributeError: atributo somente para leitura

'''

class SoLeitura(object):
    def __init__(self, nome_atr):
        self.nome_atr = nome_atr
    def __get__(self, instance, owner):
        return getattr(instance, self.nome_atr)
    def __set__(self, instance, value):
        raise AttributeError('atributo somente para leitura')

class C(object):
    def __init__(self, x):
        self._x = x
    x = SoLeitura('_x')
