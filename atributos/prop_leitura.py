'''

    >>> o = C(7)
    >>> o.x
    7
    >>> o.x = 8
    Traceback (most recent call last):
      ...
    AttributeError: can't set attribute
    >>> o._C__x
    7
    >>> o._C__x = 9
    >>> o.x
    9

'''

class C(object):
    def __init__(self, x):
        self.__x = x
    @property
    def x(self):
        return self.__x