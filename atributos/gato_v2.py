# coding: utf-8


"""
Registro de gato em um Pet Shop::

    >>> felix = Gato('Felix')
    >>> felix.nome
    'Felix'
    >>> felix.idade
    0
    >>> print felix
    Felix (0)

Agora vamos tentar atribuir uma ``idade`` a Felix::

    >>> felix.idade = 5
    Traceback (most recent call last):
      ...
    AttributeError: can't set attribute


Todo gato tem uma data de nascimento, cujo valor default é a data da
instanciação do objeto (neste caso, hoje)::

    >>> felix.dt_nasc == date.today()
    True

Se a data de nascimento não for hoje, a idade pode ser maior que zero::

    >>> tom = Gato('Tom', date(1940, 4, 13))
    >>> tom.idade >= 73
    True


"""

from datetime import date
import idade

class Gato(object):

    def __init__(self, nome, dt_nasc = date.today()):
        self.nome = nome
        self.dt_nasc = dt_nasc

    def __str__(self):
        return '%s (%s)' % (self.nome, self.idade)

    @property
    def idade(self):
        return idade.idade(self.dt_nasc)



