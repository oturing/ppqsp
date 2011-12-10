#!/usr/bin/env python
# coding: utf-8

"""
Em Python os atributos de uma classe são armazenados em um `dict`, portanto
sua ordem não é preservada. Normalmente a ordem não é realmente importante.

Note no exemplo abaixo que a lista devolvida por `dir(l)` não preserva
a ordem em que foram declarados os atributos na classe `Livro`::

    >>> class LivroSimples(object):
    ...     titulo = u''
    ...     isbn = u''
    ...     autores = u''
    >>> l = LivroSimples()
    >>> dir(l) #doctest: +ELLIPSIS
    [...'autores', 'isbn', 'titulo'...]
    
Para gerar formulários automaticamente a partir da classe, é desejável
respeitar a ordem de declaração dos campos. Usando descritores e uma 
metaclasse, é possível preservar esta ordem.

    >>> class Livro(OrderedModel):
    ...     titulo = OrderedProperty()
    ...     isbn = OrderedProperty()
    ...     autores = OrderedProperty()
    >>> l2 = Livro()
    >>> l2.titulo = 'O Alienista'
    >>> l2.titulo
    'O Alienista'
    >>> list(l2)
    ['titulo', 'isbn', 'autores']
    >>> for campo in l2: print campo
    titulo
    isbn
    autores
    >>> l3 = Livro()
    >>> l3.titulo is None
    True
    >>> l4 = Livro(titulo=u'Alice', autores=[u'Carroll', u'Tenniel'], isbn=u'9781234567890')
    >>> for campo, valor in l4.iteritems():
    ...     print '%-8s: %s' % (campo, valor)
    titulo  : Alice
    isbn    : 9781234567890
    autores : [u'Carroll', u'Tenniel']
    
Os descritores têm um atributo `order` que é inicializado com um contador da 
classe `OrderedProperty` incrementado a cada nova instância. A metaclasse usa
este atributo `order` para ordenar uma lista com os nomes dos campos.

"""

from operator import attrgetter
        
class OrderedProperty(object):
    __count = 0
    
    def __init__(self):
        self.order = self.__class__.__count
        self.__class__.__count += 1
        
    def __get__(self, instance, cls):
        return getattr(instance, self.name, None)
        
    def __set__(self, instance, value):
        setattr(instance, self.name, value)
        
    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)

class OrderedMeta(type):
    def __new__(cls, name, bases, dict):
        props = []
        for key, attr in dict.items():
            if isinstance(attr, OrderedProperty):
                attr.name = '_' + key
                props.append(attr)
        cls._ordered_props = sorted(props, key=attrgetter('order'))
        return type.__new__(cls, name, bases, dict)

class OrderedModel(object):
    __metaclass__ = OrderedMeta

    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])
    
    def __iter__(self):
        return (prop.name[1:] for prop in self.__class__._ordered_props)

    def iteritems(self):
        return ((prop.name[1:], getattr(self, prop.name)) 
                for prop in self.__class__._ordered_props)


if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
