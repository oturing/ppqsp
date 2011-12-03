'''

    >>> o = C(7, 3)
    >>> o.x
    7
    >>> o.y
    3
    >>> o.x = 8
    Traceback (most recent call last):
      ...
    AttributeError: atributo somente para leitura

'''

class SoLeitura(object):
    def __init__(self, nome_atr):
        self.nome_atr = nome_atr
    def __get__(self, instance, owner):
        if (self.nome_atr.startswith('__') and
            not self.nome_atr.endswith('__')):
            prefixo = '_' + owner.__name__
        else:
            prefixo = ''
        return getattr(instance, prefixo+self.nome_atr)
    def __set__(self, instance, value):
        raise AttributeError('atributo somente para leitura')

class C(object):
    def __init__(self, x, y):
        self.__x = x
        self._y = y
    x = SoLeitura('__x')
    y = SoLeitura('_y')