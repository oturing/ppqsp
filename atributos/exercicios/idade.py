# coding: utf-8

"""
    >>> idade(date(2000, 1,  1), date(2000, 1, 1))
    0
    >>> idade(date(2000, 1,  1), date(2001, 1, 1))
    1
    >>> idade(date(2000, 1,  1), date(2001, 12, 31))
    1
    >>> idade(date(2000, 1,  1), date(2002, 1, 1))
    2
    >>> idade(date(2000, 2, 28), date(2001, 2, 28))
    1
    >>> idade(date(2000, 2, 28), date(2001, 2, 27))
    0
    >>> idade(date(2000, 2, 28), date(2001, 3, 1))
    1
    >>> idade(date(2000, 2, 28), date(2004, 2, 29))
    4
    >>> idade(date(2000, 2, 29), date(2001, 2, 28))
    0
    >>> idade(date(2000, 2, 29), date(2001, 3, 1))
    1
    >>> idade(date(2000, 2, 29), date(2004, 2, 29))
    4
"""

from datetime import date

def idade(nascimento, hoje=None): # mudar o hoje é util para testar
    hoje = hoje or date.today()
    try:
        niver = nascimento.replace(year=hoje.year)
    except ValueError:
         # acontece qd. nascimento = 29/fev e ano atual não é bissexto
        niver = date(hoje.year, 3, 1)
    anos = hoje.year - nascimento.year
    return anos if niver <= hoje else anos - 1
