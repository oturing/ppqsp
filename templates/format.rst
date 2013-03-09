Para formatar valores, Python tem três mecanismos principais:

- o operador ``fmt % o``, inspirado pela função ``sprintf`` da linguagem C
- a função ``format(o, fmt)``, para formatar um único valor
- o método ``fmt.format(...)``, para formatar e inserir valores em uma string

Nos três casos acima, ``fmt`` é a string que define o gabarito formatação.

O método ``str.format`` é o mais flexível: aceita vários argumentos posicionais
ounomeados. Para cada argumento de ``str.format``, a função ``format`` é invocada
e o resultado encaixado nos locais indicados por ``{}`` no gabarito de
formatação.

Primeiro, alguns exemplos da função ``format`` e seus equivalentes com ``%``::

    >>> import math
    >>> format(math.pi, '6.3f')
    ' 3.142'
    >>> '%6.3f' % math.pi
    ' 3.142'
    >>> n = 12345678.9876
    >>> format(n,'18.2f')
    '       12345678.99'
    >>> '%18.2f' % n
    '       12345678.99'

Algumas operações da função ``format`` não podem ser feitas somente com ``%``::

    >>> s = 'Fotografia'
    >>> format(s,'.<16')
    'Fotografia......'
    >>> s.ljust(16, '.')
    'Fotografia......'
    >>> format(s, '.>16')
    '......Fotografia'
    >>> s.rjust(16, '.')
    '......Fotografia'
    >>> format(s ,'.^16')
    '...Fotografia...'
    >>> s.center(16, '.')
    '...Fotografia...'

Porém a função ``format`` apenas formata um valor de cada vez. Para formatar
vários valores, intercalando-os em uma string com partes constantes, usa-se
o método ``str.format``, ou o operador ``%``::

    >>> fmt = '{0} com 4 casas: {0:.4f}'
    >>> fmt.format(math.pi)
    '3.14159265359 com 4 casas: 3.1416'
    >>> '%s com 4 casas: %.4f' % (math.pi, math.pi)
    '3.14159265359 com 4 casas: 3.1416'
    >>> fmt2 = '{0} com {n:02} casas: {0:.{n}f}'
    >>> fmt2.format(math.pi, n=5)
    '3.14159265359 com 05 casas: 3.14159'
    >>> fmt2.format(math.pi, n=3)
    '3.14159265359 com 03 casas: 3.142'
    >>> '%s com %02d casas: %.*f' % (math.pi, 3, 3, math.pi)
    '3.14159265359 com 03 casas: 3.142'

Na primeira posição dentro dos marcadores ``{}`` usamos números para
indicar um argumento posicional::

    >>> '{0} {1} {2}'.format(2, 3, 5)
    '2 3 5'
    >>> '{} {} {}'.format(2, 3, 5) # Python ≥ 2.7
    '2 3 5'
    >>> '%d %d %d' % (2, 3, 5)
    '2 3 5'
    >>> '{2} {1} {0}'.format(2, 3, 5)
    '5 3 2'
    
Se argumento selecionado tem atributos, eles também podem ser acessados::    
    
    >>> '{0.real} {0.imag}'.format(3j+4)
    '4.0 3.0'
    >>> '%s %s' % ((3j+4).real, (3j+4).imag)
    '4.0 3.0'
    >>> '{0.real:f} {0.imag:f}'.format(3j+4)
    '4.000000 3.000000'
    >>> '%f %f' % ((3j+4).real, (3j+4).imag)
    '4.000000 3.000000'
    
Se o método ``str.format`` recebe argumentos nomeados, os nomes podem ser
usados nos marcadores diretamente, como em uma linguagem de templates::
    
    >>> 'Euro: {EUR}, Real: {BRL}'.format(BRL=0.5, EUR=1.3)
    'Euro: 1.3, Real: 0.5'
    >>> d = {'BRL':0.5457, 'EUR':1.3496}
    >>> 'Euro: {EUR}, Real: {BRL}'.format(**d)
    'Euro: 1.3496, Real: 0.5457'
    >>> 'Euro: {0[EUR]}, Real: {0[BRL]}'.format(d)
    'Euro: 1.3496, Real: 0.5457'

Com ``%`` fica assim::

    >>> 'Euro: %(EUR)s, Real: %(BRL)s' % d
    'Euro: 1.3496, Real: 0.5457'
    
Mais exemplos de acesso a itens e atributos::    
    
    >>> from datetime import date
    >>> dts = (date(2011,9,3), date(2011,9,7))
    >>> 'de {0[0].day} a {0[1].day}'.format(dts)
    'de 3 a 7'
    >>> 'de {0.day} a {1.day}'.format(*dts)
    'de 3 a 7'
    >>> 'de {.day} a {.day}'.format(*dts) # ≥ 2.7
    'de 3 a 7'
    >>> 'de %s a %s' % (dts[0].day, dts[1].day)
    'de 3 a 7'
    
Se o objeto a ser formatado tem um método ``__format__``, este método
recebe a string de formatação para interpretar. Isso significa que
a notação de formatação é extensível por classes criadas pelo programdor!
    
::
    
    >>> class Spam(object):
    ...     def __str__(self):
    ...         return 'Spam!!!'
    ...     def __format__(self, fmt):
    ...         return 'Spam'.replace(fmt, fmt*3)
    >>> s = Spam()
    >>> '{0!s}, {0!r}'.format(s) #doctest:+ELLIPSIS
    'Spam!!!, <__main__.Spam object at ...>'
    >>> '{0}, {0:a}, {0:m}'.format(s)
    'Spam, Spaaam, Spammm'

Mais exemplos variados::

    >>> format(math.pi, '_>+8.3f')
    '__+3.142'
    >>> format(math.pi, '_=+8.3f')
    '+__3.142'
    >>> format(123, '0= 6x')
    ' 0007b'
    >>> format(123, '0=+6x')
    '+0007b'
    >>> format(123, '#06x')
    '0x007b'
    >>> '{0:f} {0:e}'.format(2**32)
    '4294967296.000000 4.294967e+09'
    >>> '%f %e' % (2**32, 2**32)
    '4294967296.000000 4.294967e+09'
    >>> '{0:{1}} {0:{2}}'.format(2**32, 'f', 'e')
    '4294967296.000000 4.294967e+09'
    >>> format(12345678.9876,'18.10n')
    '       12345678.99'

Na notação de ``format``, o sinal ``%`` indica porcentagem (o valor numérico
é multiplicado por 100 para exibição)::

    >>> n, t = 15, 42
    >>> '{}/{} ({:.1%})'.format(n, t, float(n)/t)
    '15/42 (35.7%)'
    >>> '%s/%s (%0.1f%%)' % (n, t, float(n)/t * 100)
    '15/42 (35.7%)'
    
O próprio código do formato pode ser parametrizado recursivamente::
    
    >>> '{a:{b}}'.format(a=2**64, b='e')
    '1.844674e+19'
    >>> format(2**64,'e')
    '1.844674e+19'

Quando o ``locale`` suporta, é possível exibir separadores de milhares::

    >>> from locale import setlocale, LC_NUMERIC
    >>> setlocale(LC_NUMERIC, 'de_DE.UTF-8')
    'de_DE.UTF-8'
    >>> # http://bugs.python.org/issue16944
    >>> format(12345678.9876,'18.10n') # doctest: +SKIP
    '     12.345.678,99'
