#!/usr/bin/env python
# coding: utf-8

"""
Cálculos de idade::

    >>> hoje = date(2009, 2, 28)
    >>> idade(date(2008, 2, 28), hoje)
    1
    >>> idade(date(2008, 2, 29), hoje)
    0
    >>> idade(date(2000, 1, 1), hoje)
    9

Idades com meses::

    >>> nasc = date(2000, 5, 10)
    >>> idade_meses(nasc, date(2001, 5, 10))
    (1, 0)
    >>> idade_meses(nasc, date(2001, 9, 10))
    (1, 4)
    >>> idade_meses(nasc, date(2001, 9, 9))
    (1, 3)
    >>> idade_meses(nasc, date(2001, 4, 10))
    (0, 11)
    >>> idade_meses(nasc, date(2001, 4, 9))
    (0, 10)

"""

from datetime import date

def idade(nascimento, quando=None):
    if quando is None:
        quando = date.today()
    anos = quando.year - nascimento.year
    if (nascimento.month, nascimento.day) > (quando.month, quando.day):
        anos -= 1
    return anos

def idade_meses(nascimento, quando=None):
    if quando is None:
        quando = date.today()
    anos = idade(nascimento, quando)
    meses = quando.month - nascimento.month
    if nascimento.day > quando.day:
        meses -= 1
    if meses < 0:
        meses = 12 + meses
    return (anos, meses)


