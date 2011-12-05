
=============================
Python para quem sabe Python
=============================

----------------------
Lista de exercícios 1
----------------------

1. Baralho polimórfico
=======================

Para os exercícios desta seção, use como base o código do exemplo `baralho.py`_.

.. _baralho.py: https://github.com/oturing/ppqsp/blob/master/iteraveis/baralho.py

1.1. Implemente uma subclasse de Baralho chamada BaralhoInverso com um método
``__iter__`` que produz um iterador para fornecer as cartas na ordem inversa,
ou seja, antes de embaralhar, primeira carta deve ser o ``<K de paus>`` em vez
do ``<A de copas>``, como acontece na implementação atual.

**Bônus:** implemente três métodos, ``iter_genexp``, ``iter_genfun`` e
``iter_obj``, usando (respectivamente) uma expressão geradora, uma função
geradora e um objeto iterador.

1.2. Implemente uma subclasse de Baralho chamada BaralhoMisturado com um
método ``__iter__`` que produz um iterador para fornecer as cartas em uma
ordem aleatória. Note que este iterador deverá produzir exatamente 52 cartas,
e nenhuma deverá ser repetida. Seguindo as filosofia do padrão de projeto
Iterator, o iterador não deve alterar o estado interno do baralho, de modo que
possam existir dois iteradores ao mesmo tempo, cada um percorrendo as cartas
embaralhadas de em uma ordem diferente.

**Dicas:** (1) não embaralhe a estrutura interna que contém as cartas, mas
gere uma série embaralhada de índices, e use esta série para determinar a
próxima carta; (2) use a função ``shuffle`` do módulo ``random`` para
embaralhar os índices.

2. List comprehensions (*listcomps*)
=====================================

Para estes exercícios, usaremos as listas abaixo::

    mulheres = ['Mariana', 'Ana', 'Paula']
    homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']

2.1. Use uma *listcomp* para gerar uma lista de homens com nomes de 4 ou menos
letras.

2.2. Use uma *listcomp* para gerar uma lista de duplas (também conhecida em
computação como uma lista associativa) formada pela letra inicial e o nome de
cada homem. Por exemplo, a resposta para a lista ``mulheres`` seria::

    [('M', 'Mariana'), ('A', 'Ana'), ('P', 'Paula')]

2.3. Use o resultado do exercício 2.2 para gerar um dicionário associando
iniciais aos nomes de homens. Quantos itens terá o dicionário assim produzido?

2.4. Use a função ``zip`` para gerar uma lista associativa, e com ela carregar
um dicionário associando cada mulher a um homem. Quantos itens terá o
dicionário assim produzido?

2.5. **Bônus:** Gere uma lista associativa para organizar uma aula de dança na qual todos
devem dançar com todos. Quantos casais serão formados?

**Dica:** o nome da operação a ser feita neste exercício é *produto
cartesiano*, e para fazer isso em uma *listcomp* ou *genexp* você precisa usar
mais de um ``for`` dentro da expressão.

2.6. **Bônus:** Repita o exercício 2.5, acrescentando um filtro com ``if`` para remover os nomes com
menos de 4 letras das duas listas. Quantos casais serão formados?


3. Biblioteca padrão
=====================

3.1. "The quick brown fox jumps over the lazy dog" é um pangrama, uma frase
que usa todas as letras do alfabeto inglês.

O que faz o código abaixo? Qual a resposta que aparece no lugar de «1»? ::

    >>> fox = 'The quick brown fox jumps over the lazy dog.'
    >>> fox_letters = set(l.upper() for l in q if l.isalpha())
    >>> len(fox_letters)
    «1»

3.2. Que resposta apareceria no lugar de «1» se não fosse usado o filtro
`if` na expressão geradora acima?

3.3. Para verificar se o conjunto ``fox_letters`` realmente contém todas as
letras do alfabeto, podemos verificar este conjunto é igual ao conjunto das
letras ASCII maíusculas que o Python conhece. Para fazer esta verificação, o
que devemos escrever no lugar de «1», e que resposta aparecerá em «2»? ::

    >>> import string
    >>> letters = set(string.ascii_uppercase)
    >>> «1» == letters
    «2»

3.4. O alfabeto português antigamente era menor que o inglês, mas hoje é igual
(tirando o cedilha). A frase abaixo aparece como exemplo de pangrama na
Wikipédia em português, vamos verificar usando a mesma técnica usada acima,
substituindo «1», «2» e «3» pelas expressões apropriadas::

    >>> jabuti = 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
    >>> jabuti_letras = set(«1» for l in «2» if «3»)

Uma vez que temos o conjunto das letras da frase do jabuti, podemos verificar
a diferença entre o conjunto de todas as letras e este conjunto. Qual operador
usamos em «1» e qual a resposta aparecerá em «2»::

    >>> letters «1» jabuti_letras
    set(«2»)

**Bônus:** Existem dois operadores de conjunto que podem ser usados no lugar
de «1», e neste exemplo ambos produziriam o mesmo resultado em «2». Quais são
os operadores, e qual a diferença entre eles?

4. Funções redutoras
=====================

Para os exemplos abaixo, usaremos as listas `m` e `n`::

    m = [5, 3, 7, 2, 0, -1]
    n = [10, 20, 30]

4.1. Complete as lacunas «?» nestas aplicações simples de funções redutoras::

    >>> all(m)
    «1»
    >>> all(n)
    «2»
    >>> any(m)
    «3»
    >>> any(n)
    «4»
    >>> sum(«5»)
    60
    >>> sum(«6»)
    76

4.4. Calcule o resultado «1»::

    >>> sum(a*b for (a,b) in enumerate(n))
    «1»

4.3. Explique o resulado abaixo::

    >>> all(x for (x,y) in zip(m, n))
    True

4.4. Calcule o resultado «1»::

    >>> sum(x*y for (x,y) in zip(m, n))
    «1»

5. Explorando o protocolo de ``Sequence``
==========================================

5.1 Descrição do problema
--------------------------

Na turma 0 do curso *Python para quem sabe Python*, o participante João Paulo
Dubas sugeriu um exemplo para explorar o procolo (ou *interface*) da classe
abstrata ``collections.Sequence`` introduzida no Python 2.6. Este exercício é
baseado no exemplo proposto pelo João Paulo.

Pela documentação do Python, e pelo UML mostrado em aula, notamos que a classe
``Sequence`` declara ``__getitem__`` como método abstrato, mas fornece como
*mixins* os métodos ``__contains__``, ``__iter__``, ``__reversed__``,
``index``, e ``count``.

Isso significa que uma subclasse concreta de ``Sequence`` só precisa
implementar ``__getitem__`` para poder herdar automaticamente as
implementações dos 5 métodos mixins que mencionados acima.

Claro que esta conveniência tem um preço, afinal não existe almoço de graça
(até no *Bom Prato* custa R$ 1). O preço é que a implementação possível para
``__contains__``, ``index`` e ``count``, a partir apenas da funcionalidade do
``__getitem__`` envolverá necessariamente uma busca linear.

Por exemplo, considerando um uma subclasse concreta ``ListaOrdenada`` de
``Sequence``, implementando apenas o método ``__getitem__``, vamos criar uma
instância ``lo`` de ``ListaOrdenada``, contendo um milhão de itens::

    >>> lo = ListaOrdenada(range(10**6))

Para avaliar a expressão abaixo, Python acionará o método ``__contains___``,
herdado de ``Sequence``::

    >>> 500000 in lo
    True

Porém, como a implementação *mixin* de ``__contains___`` só pode contar com a
implementação concreta de ``__getitem__``, para responder a pergunta acima
Python terá que percorrer 500.000 itens. E para esta outra pergunta, Python
terá que percorrer todos os 1.000.000 de itens::

    >>> -1 in lo
    False

Porém, sabendo que os itens de uma ``ListaOrdenada`` estão em ordem
ascendente, é possível fazer uma implementação muito mais eficiente de
``__contains___``, usando uma busca binária.

5.2 Sua missão
---------------

No repositório ``/oturing/ppqsp`` do GitHub você encontrará um módulo
`lista_ord.py`_, que implementa uma classe ``ListaOrdenada(Sequence)``. No
mesmo diretório há um módulo `busca_bin.py`_ que contém uma função
``busca_bin`` que faz a busca binária de um item em uma sequência ordenada.

.. _lista_ord.py: https://github.com/oturing/ppqsp/blob/master/iteraveis/lista_ord.py
.. _busca_bin.py: https://github.com/oturing/ppqsp/blob/master/iteraveis/busca_bin.py

Sua missão é usar a função ``busca_bin`` para implementar o método
``__contains__`` na classe ``ListaOrdenada``. Assegure-se de que os *doctests*
do módulo ``lista_ord.py`` continuam passando, e use a função ``desempenho``
do mesmo módulo para verificar se a sua implementação realmente ficou mais
rápida que a original.

5.3. Missão bônus
------------------

Na verdade, a função ``busca_bin`` faz mais do que dizer se o item existe: ela
informa a posição do item. Aproveitando este fato, refatore o código do
exercício 5.2 para implementar primeiro o método ``ListaOrdenada.index``,
respeitando a convenção de que ``index`` levanta ``ValueError`` se o item não
existe na sequência. Recomendo fazer TDD, ou seja, implemente primeiro o teste
para o caso mais simples possível do método ``index``, verifique que o teste
não passa, e então implemente o método para fazer este teste passar. Continue
assim: implemente um teste adicional, acrescente funcionalidade para passar o
teste, refatore se necessário.

Uma vez implementando ``index``, rafatore ``ListaOrdenada.__contains__`` para
usar o método ``ListaOrdenada.index`` (evitando duplicação de código). Isso
não vai exigir novos testes, mas apenas assegure-se de que os testes
anteriores continuam passando.

E finalmente, usando TDD, implemente uma versão eficiente do método
``ListaOrdenada.count`` que devolve a quantidade de ocorrências de um item em
uma ``ListaOrdenada``. Seu primeiro teste deve verificar o caso mais simples:
se ``count`` devolve 0 quando o item não ocorre na lista. Depois implemente
testes e a funcionalidade para quando só existe um item, e só então ataque o
problema de vários itens, sempre escrevendo o teste primeiro.

----

**Bom trabalho!**

Qualquer dúvida, nos falamos pelo grupo `OTuring`_!

.. _OTuring: http://groups.google.com/group/oturing

*Luciano Ramalho*
