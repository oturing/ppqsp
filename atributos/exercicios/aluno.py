# coding: utf-8

"""
Neste exemplo temos uma classe `Aluno` que é inicializada com um nome
e uma data de nascimento em formato ISO-8601. O atributo `nascimento` é
uma property ou descritor que armazena e devolve um objeto `datetime.date`::

    >>> a = Aluno('Juca', '2000-06-10')
    >>> a.nome
    'Juca'
    >>> a.nascimento
    datetime.date(2000, 6, 10)

Além da propriedade read/write `nascimento`, instâncias de aluno têm uma
propriedade read-only chamada `idade` que devolve o número de anos completos
desde o nascimento até hoje. Para implementar esta propriedade, usamos a
função `idade` do módulo `idade.py` presente neste diretório.

A seguir, testamos a função `idade.idade`, como se hoje fosse o dia
20/6/2010::

    >>> idade(date(2009,6,20))
    1

Como hoje não é 20/6/2010, o exemplo acima funciona devido a um patch
explicado na função `test`.

Graças a este truque, podemos testar a propriedade `idade` do aluno como
se estivéssemos em 20/6/2010::

    >>> a.idade
    10

"""

from datetime import datetime, date
from idade import idade

class Aluno(object):
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

def test():
    """Para testar a idade, fazemos um patch no ambiente global do
    interpretador Python antes de executar os testes, substituindo a
    função `idade` importada do módulo `idade` por outra função que
    considera que hoje é sempre 20/6/2010. Veja como isso é feito na
    função `test`.
    """
    import doctest
    idade_real = idade
    def idade_fake(nasc):
        return idade_real(nasc, date(2010,6,20))
    globals()['idade'] = idade_fake # patch no ambiente global
    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    globals()['idade'] = idade_real # remover patch

if __name__=='__main__':
    test()
