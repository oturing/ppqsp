#!/usr/bin/env python
# coding: utf-8

'''
    >>> for i in [letra for letra in gera_letra()]:
    ...    print i
    ...
    gerando 'A'...
    gerando 'B'...
    gerando 'C'...
    A
    B
    C
    >>> for i in (letra for letra in gera_letra()):
    ...    print i
    ...
    gerando 'A'...
    A
    gerando 'B'...
    B
    gerando 'C'...
    C
'''

def gera_letra(ultima='C', verboso=True):
    cod = ord('A')
    while chr(cod) <= ultima:
        letra = chr(cod)
        if verboso:
            print 'gerando %r...' % letra
        yield letra
        cod += 1

if __name__=='__main__':
    import doctest
    doctest.testmod()
