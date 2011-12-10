#!/usr/bin/env python
# coding: utf-8

"""

Exemplo de uso do CheckedModel::

    >>> class Livro(CheckedModel):
    ...     titulo = SingularProperty(required=True)
    ...     isbn = SingularProperty()
    ...     autores = PluralProperty(required=True)
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
    
O método booleano `isplural` informa se o atributo nomeado é plural::

    >>> for campo in l4:
    ...     print '%-8s: %s' % (campo, l4.isplural(campo))
    titulo  : False
    isbn    : False
    autores : True

O método `iteritemsplural` devolve um iterador de triplas com o nome do campo,
o valor, e um booleano indicando se é plural, facilitando a formatação dos valores::

    >>> for campo, valor, plural in l4.iteritemsplural():
    ...     valor = '; '.join(valor) if plural else valor
    ...     print '%-8s: %s' % (campo, valor)
    titulo  : Alice
    isbn    : 9781234567890
    autores : Carroll; Tenniel

Aos descritores `PluralProperty` só é permitido atribuir tuplas, listas ou 
instâncias de subclasses destes tipos::

    >>> l5 = Livro(autores=u'Fulano')
    Traceback (most recent call last):
      ...
    TypeError: PluralProperty must satisfy isinstance(value, (tuple, list))
    >>> l5 = Livro(autores=[])

Para validar propriedades obrigatórias, há o método check::

    >>> l4.check() # livro completo, nenhuma mensagem de erro
    {}
    >>> l6 = Livro()
    >>> l6.check()
    {'titulo': u'Required value missing.', 'autores': u'Required value missing.'}
    >>> l7 = Livro(titulo=u'Jangada de Pedra')
    >>> l7.check()
    {'autores': u'Required value missing.'}
    
No caso de propriedades plurais como `autores`, `check` verifica se há pelo
menos um item na propriedade, e se este item tem conteúdo::
    
    >>> l8 = Livro(titulo=u'Jangada de Pedra', autores=[])
    >>> l8.check()
    {'autores': u'Required value missing.'}
    >>> l9 = Livro(titulo=u'Jangada de Pedra', autores=[u''])
    >>> l9.check()
    {'autores': u'Required value missing.'}
    >>> l10 = Livro(titulo=u'Jangada de Pedra', autores=[u'Saramago'])
    >>> l10.check()
    {}

Na definição de uma propriedade, pode-se passar uma função de validação que
aceita um valor e realiza um teste, devolvendo uma string vazia se o valor
passar no teste, ou uma mensagem de erro se o valor não passar::

    >>> class Produto(CheckedModel):
    ...     nome = SingularProperty(required=True)
    ...     estoque = NumberProperty(required=True)
    ...     preco = NumberProperty(validator=lambda v:u'Deve ser maior que zero' if v<=0 else '')
    >>> p1 = Produto(nome='rebimboca', estoque=0)
    >>> p1.check()
    {}
    
Neste caso o `preco` não é obrigatório, e se não for informado o seu validador
não é executado. Mas se um `preco` for definido, o validador é acionado::
    
    >>> p2 = Produto(nome='rebimboca', estoque=0, preco=0)
    Traceback (most recent call last):
      ...
    ValueError: Deve ser maior que zero
    >>> p3 = Produto(nome='rebimboca', estoque=0, preco=9.99)
    >>> p3.check()
    {}
    
Uma `SingularProperty` pode ser limitada por um vocabulário controlado::    

    >>> class Camisa(CheckedModel):
    ...     modelo = SingularProperty(required=True)
    ...     cor = SingularProperty(required=True, choices=[u'amarela', u'azul'])
    ...     tamanho = NumberProperty(required=True, choices=range(1,7))
    >>> c1 = Camisa(modelo=u'selecao', cor=u'verde')    
    Traceback (most recent call last):
      ..
    ValueError: u'verde' is not a valid choice.
    >>> c2 = Camisa(modelo=u'selecao', cor=u'azul')
    >>> c2.check()
    {'tamanho': u'Required value missing.'}
    >>> c3 = Camisa(modelo=u'selecao', cor=u'azul', tamanho=9)
    Traceback (most recent call last):
      ...
    ValueError: 9 is not a valid choice.
    
"""

from ordprops import OrderedProperty, OrderedModel
        
class SingularProperty(OrderedProperty):

    def __init__(self, required=False, validator=None, choices=None):
        super(SingularProperty, self).__init__()
        self.required = required
        self.validator = validator
        self.choices = choices if choices else []

    def __set__(self, instance, value):
        msg = self.check(value)
        if msg:
            raise ValueError(msg)    
        else:
            setattr(instance, self.name, value)

    def check(self, value):
        if value is not None:        
            if self.validator:
                return self.validator(value)
        if self.choices and value not in self.choices:
            return u'%r is not a valid choice.' % value
                
    def missing(self, instance): # missing or blank
        return self.required and not getattr(instance, self.name, None)

class NumberProperty(SingularProperty):

    def __set__(self, instance, value):
        if not isinstance(value, (int, long, float)):
            raise TypeError('NumberProperty must be int, long or float')
        msg = self.check(value)
        if msg:
            raise ValueError(msg)    
        else:
            setattr(instance, self.name, value)

    def missing(self, instance):                
        return self.required and getattr(instance, self.name, None) is None

class PluralProperty(SingularProperty):

    def __set__(self, instance, value):
        if isinstance(value, (tuple, list)):
            setattr(instance, self.name, value)
        else:
            raise TypeError('PluralProperty must satisfy isinstance(value, (tuple, list))')

    def missing(self, instance):                
        if self.required:
            value = getattr(instance, self.name, None)
            if value is None or len(value) == 0 or not value[0]:
                return True

class CheckedModel(OrderedModel):

    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])
    
    def __iter__(self):
        return (prop.name[1:] for prop in self.__class__._ordered_props)

    def iteritems(self):
        return ((prop.name[1:], getattr(self, prop.name)) 
                for prop in self.__class__._ordered_props)
                
    def isplural(self, name):
        return isinstance(self.__class__.__getattribute__(self.__class__, name), PluralProperty)

    def iteritemsplural(self):
        return ((prop.name[1:], getattr(self, prop.name), self.isplural(prop.name[1:]))
                for prop in self.__class__._ordered_props)

    def check(self):
        msgs = {}
        for prop in self:
            descriptor = self.__class__.__getattribute__(self.__class__, prop)
            if descriptor.missing(self):
                msg = u'Required value missing.'
            else:
                msg = descriptor.check(getattr(self, prop))
            if msg:
                msgs[prop] = msg
        return msgs            


if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
