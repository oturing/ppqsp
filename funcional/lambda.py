'''

>>> dobro = lambda n: n * 2
>>> dobro(7)
14

>>> lista = [1, 2, 3, 4, 5]
>>> reduce(lambda a, b: a+b, lista)
15
>>> from operator import add, mul
>>> reduce(add, lista)
15
>>> sum(lista)
15
>>> reduce(mul, lista)
120
>>> fat = lambda x: 1 if x < 2 else reduce(mul, range(x,1,-1))
>>> fat(5)
120


'''