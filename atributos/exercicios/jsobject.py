# coding: utf-8

"""

(1) Instâncias de `JSObj` imitam o comportamento de objetos JavaScript.
Você pode criar uma instância e pendurar nela os atributos que quiser,
como em Python::

    >>> o = JSObj()
    >>> o.num = 10
    >>> o.num
    10

(2) Porém, diferente de objetos Python comuns, os atributos de uma
instância de `JSObj` podem ser acessados como se ela fosse um dicionário::

    >>> o['num']
    10

(3) Além disso, atributos podem ser modificados usando a mesma notação::

    >>> o['num'] = 13
    >>> o.num
    13

(4) Em JavaScript, novos atributos podem ser criados usando as duas
notações (`.` e `[]`), mas neste exercício vamos impedir a criação de
novos atributos via notação de `[]`:

    >>> o['nome'] = 'Lara'
    Traceback (most recent call last):
      ...
    TypeError: attributes can only be created using .dot notation

(5) A função `len` pode ser usada para determinar o número de atributos
de um `JSObj`::

    >>> len(o)
    1

(6) Um `JSObj` pode ser construído a partir de um dicionário::

    >>> sp = JSObj({'lat': 23.55, 'long': 46.63})
    >>> sp.lat, sp.long
    (23.55, 46.63)

(7) O construtor também pode ser invocado com argumentos nomeados::

    >>> contato = JSObj(nome='Fred', fone='4321-1234')

Imitar o comportamento de um `dict` permite aproveitar melhor o operador
de formatação de strings `%`:

    >>> '%(nome)s: %(fone)s' % contato
    'Fred: 4321-1234'

(8) A representação de um `JSObj` imita uma invocação do construtor,
permitindo a reconstrução do objeto via `eval`::

    >>> o
    JSObj({'num': 13})

(9) O operador `==` é sobrecarregado para comparar os atributos de dois
`JSObj`::

    >>> sp == JSObj(lat=23.55, long=46.63)
    True

Implementamos o `==` para poder testar se o `repr` realmente funciona
com `eval`, como prometido no passo (8)::

    >>> sp == eval(repr(sp))
    True

"""

class JSObj(object):
    """Uma classe que imita objetos JavaScript"""

def test():
    import doctest
    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)

if __name__=='__main__':
    test()
