'''

>>> class Auto():
...     def __init__(self, modelo, ano):
...         self.modelo = modelo
...         self.ano = ano
...     def __repr__(self):
...         return '<Auto %(modelo)r, %(ano)s>' % self.__dict__
>>> a6 = Auto('Audi A6', 2007)
>>> merc = Auto('Mercedes S6', 2001)
>>> fusca = Auto('Fusca 1600', 1966)
>>> carros = [fusca, merc, a6]
>>> carros.sort()
>>> carros
[<Auto 'Audi A6', 2007>, <Auto 'Mercedes S6', 2001>, <Auto 'Fusca 1600', 1966>]
>>> carros.sort(lambda a,b: cmp(a.ano, b.ano))
>>> carros
[<Auto 'Fusca 1600', 1966>, <Auto 'Mercedes S6', 2001>, <Auto 'Audi A6', 2007>]
>>> sorted(carros, key=lambda carro: carro.modelo)
[<Auto 'Audi A6', 2007>, <Auto 'Fusca 1600', 1966>, <Auto 'Mercedes S6', 2001>]
>>> from operator import attrgetter
>>> sorted(carros, key=attrgetter('modelo'))
[<Auto 'Audi A6', 2007>, <Auto 'Fusca 1600', 1966>, <Auto 'Mercedes S6', 2001>]
>>> sorted(carros, key=attrgetter('ano'))
[<Auto 'Fusca 1600', 1966>, <Auto 'Mercedes S6', 2001>, <Auto 'Audi A6', 2007>]
>>> f = attrgetter('ano')
>>> f(fusca)
1966
>>> f(merc)
2001

'''