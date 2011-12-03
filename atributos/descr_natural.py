'''
    >>> o = C(7)
    >>> o.x
    7
    >>> o._x
    7
    >>> o.x = 0
    Traceback (most recent call last):
      ...
    TypeError: valor deve ser >= 1
    >>> o = C(-3)
    Traceback (most recent call last):
      ...
    TypeError: valor deve ser >= 1
    >>> class D(object):
    ...     def __init__(self, x):
    ...         self.x = x
    ...     x = Natural('x', True)
    >>> u = D(0)
    >>> u.x
    0

'''

class Natural(object):
    def __init__(self, nome_atr, inclui_zero=False):
        self.nome_atr = nome_atr
        self.minimo = 0 if inclui_zero else 1
    def __get__(self, instance, owner):
        return getattr(instance, '_'+self.nome_atr)
    def __set__(self, instance, value):
        if value >= self.minimo:
            setattr(instance, '_'+self.nome_atr, int(value))
        else:
            msg = 'valor deve ser >= %s'
            raise TypeError(msg % self.minimo)

class C(object):
    def __init__(self, x):
        self.x = x
    x = Natural('x')
