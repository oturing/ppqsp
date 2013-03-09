# coding: utf-8

"""
(1) Neste exemplo temos uma classe `Contato` que é inicializada com um
nome e um e-mail::

    >>> c = Contato('Juca', 'juca@lab.tmp.br')
    >>> c.nome
    'Juca'
    >>> c.email
    'juca@lab.tmp.br'


(2) O atributo `email` é uma property ou descritor que aceita apenas
e-mails válidos::

    >>> c.email = 'x'
    Traceback (most recent call last):
      ...
    ValueError: e-mail invalido 'x'

(3) A validação ocorre também ao instanciar um novo 'Contato'::

    >>> c = Contato('Yoli', 'y@y')
    Traceback (most recent call last):
      ...
    ValueError: e-mail invalido 'y@y'

"""

from email import is_valid

class Contato(object):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

def test():
    import doctest
    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)

if __name__=='__main__':
    test()
