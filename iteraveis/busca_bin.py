# coding: utf-8

# Código testado com Python 2.7, 3.2, PyPy(1.7) 2.7 e Jython 2.5.2

"""
    >>> l = []
    >>> busca_bin(l, 0)
    -1
    >>> l = [7]
    >>> [busca_bin(l, x) for x in [0, 7, 8]]
    [-1, 0, -1]
    >>> l = [2, 4]
    >>> [busca_bin(l, x) for x in l]
    [0, 1]
    >>> [busca_bin(l, x) for x in [1, 3, 5]]
    [-1, -1, -1]
    >>> l = [1, 3, 5]
    >>> [busca_bin(l, x) for x in l]
    [0, 1, 2]
    >>> [busca_bin(l, x) for x in [0, 2, 4, 6]]
    [-1, -1, -1, -1]
    >>> l = [1, 2, 3, 4]
    >>> [busca_bin(l, x) for x in l]
    [0, 1, 2, 3]
    >>> [busca_bin(l, x) for x in [0, 1.5, 4.1]]
    [-1, -1, -1]

"""

try:
    xrange
except NameError:
    xrange = range # para funcionar no Python 3

def busca_bin(seq, item):
    """Assumindo que `seq` está ordenada, devolve a posição do `item`.

    Se `item` não está presente em `seq`, devolve -1.
    """
    a, b = 0, len(seq)
    i = -1
    while (a < b):
        i_ant = i
        i = (a+b)//2
        if i == i_ant:
            break
        atual = seq[i]
        if item == atual:
            return i
        elif item < atual:
            b = i
        else:
            a = i
    return -1

def busca_lin_enum(seq, item):
    for i, valor in enumerate(seq):
        if valor == item:
            return i
    return -1

def busca_lin_for(seq, item):
    for i in xrange(len(seq)):
        if seq[i] == item:
            return i
    return -1

def busca_lin_while(seq, item):
    i = 0
    while i < len(seq):
        if seq[i] == item:
            return i
        i += 1
    return -1

def busca_index(seq, item):
    try:
        return seq.index(item)
    except ValueError:
        return -1

def desempenho():
    import sys
    from timeit import Timer
    print(sys.version)
    tam = 10**6
    expr = '''b(l, %d), b(l, %d), b(l, %d)''' % (0, tam/2, tam)
    for nome_busca in (k for k in sorted(globals()) if k.startswith('busca')):
        prep = '\n'.join([
            '''from __main__ import %s as b\n''' % nome_busca,
            '''l = list(range(%d))''' % tam]) # Python 2 e 3: list(range(n))
        res = min(Timer(expr, prep).repeat(number=10))
        print('%15s: %12.8f' % (nome_busca, res))

def teste():
    import doctest
    return doctest.testmod()[0] # devolver falhas

if __name__=='__main__':
    falhas = teste()
    if not falhas:
        desempenho()
