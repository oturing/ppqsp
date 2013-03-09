
=============================
Python para quem sabe Python
=============================

----------------------
Lista de exercícios 2
----------------------

1. Contato com e-mail válido
=============================

O objetivo deste exercício é fazer passar os doctests do exemplo
`contato.py`_, onde encontramos uma classe `Contato` que tem um atributo
`email` que deve verificar a sintaxe do endereço atribuído.

1.1. Baixe os arquivos `contato.py`_ e `email.py`_ e execute o primeiro
como um script. Você verá este resultado::

    $ python contato.py
    **********************************************************************
    File "contato.py", line 17, in __main__
    Failed example:
        c.email = 'x'
    Expected:
        Traceback (most recent call last):
          ...
        ValueError: e-mail invalido 'x'
    Got nothing
    **********************************************************************
    1 items had failures:
       2 of   5 in __main__
    ***Test Failed*** 2 failures.

.. _contato.py: https://github.com/oturing/ppqsp/blob/master/atributos/exercicios/contato.py

.. _email.py: https://github.com/oturing/ppqsp/blob/master/atributos/exercicios/email.py

1.2. Observe que o relatório indica que aconteceram duas falhas, mas apenas
uma está sendo exibida em detalhes.

Examine o arquivo `contato.py`_ para entender seu funcionamento.  Os testes
são executados pela função `test()`. Nela usamos a opção
``doctest.REPORT_ONLY_FIRST_FAILURE``. Isso foi feito para facilitar a sua progressão no
exercício: a cada etapa, apenas o primeiro erro é detalhado, orientando a
implementação passo-a-passo da solução.

Note também que os parágrafos da docstring são numerados (1), (2)... para que
possamos nos referir aos respectivos grupos de testes.

1.3. Para passar o teste do parágrafo (2) você precisará implementar uma
property com getter e setter. **Dica**: use os decoradores `@property` e
`@email.setter`. Para relembrar veja o slide 10 da apresentação *PPQSP Turma
1, Aula 3* (`ppqsp_t1a3.pdf`_)

.. _ppqsp_t1a3.pdf: http://turing.com.br/material/ppqsp/ppqsp_t1a3.pdf

1.4. Dependendo de como você implementou o item 1.3, talvez o teste da 
validação na instanciação parágrafo (3) já esteja passando. Se isso 
acontecer, explique porquê. Do contrário, implemente o que for preciso 
para que o teste (3) passe.

1.5. **Bônus:** Copie o arquivo `contato.py` para `contato2.py` e refaça o
exercício neste novo arquivo usando um descriptor em vez de property. **Dica**:
aproveite a classe `ValidatedDescriptor` que criamos no exemplo
`pedido4.py`_ durante o curso.

.. _pedido4.py: https://github.com/oturing/ppqsp/blob/master/atributos/metaclasses/pedido4.py

2. Aluno com data de nascimento e idade
========================================

Neste exercício vamos trabalhar com dois atributos relacionados: um read/write
(leitura e escrita) e outro read-only (apenas leitura). Além de ilustrar
atributos relacionados, este exercício mostra o uso de uma técnica para
automação de testes que dependem da data atual.

O exemplo é uma classe `Aluno` bem simples, com atributos `nome` e
`nascimento`. O atributo `nascimento` contem uma instância de `datetime.date`.
Um terceiro atributo, `idade` é calculado a partir da dada de nascimento,
levando em consideração a data atual.

2.1. Baixe os arquivos `aluno.py`_ e `idade.py`_ e execute o primeiro
como um script. O resultado inicial é::

    $ python aluno.py
    **********************************************************************
    File "aluno.py", line 11, in __main__
    Failed example:
        a.nascimento
    Expected:
        datetime.date(2000, 6, 10)
    Got:
        '2000-06-10'
    **********************************************************************
    1 items had failures:
       2 of   5 in __main__
    ***Test Failed*** 2 failures.

.. _aluno.py: https://github.com/oturing/ppqsp/blob/master/atributos/exercicios/aluno.py

.. _idade.py: https://github.com/oturing/ppqsp/blob/master/atributos/exercicios/idade.py

2.2. Implemente uma property com getter e setter para o atributo `nascimento`.
O setter desta property deve aceitar uma string de data em formato ISO-8601
(YYYY-MM-DD) e armazenar um objeto `datetime.date` construído a partir da
string. O getter simplesmente devolve o objeto `date` armazenado, como
ilustrado pelo teste.

**Dicas**: você pode usar o método ``datetime.strptime(data, '%Y-%m-%d')`` para
produzir uma instância de `datetime` a partir da string, e usar os atributos 
`year` , `month` e `day` desta instância para construir um objeto `date`. Outra
alternativa é analisar com `split` e `int` a string fornecida para construir a 
`date`. Faça como achar melhor.

2.3. Estude o código do teste (2). Note que ele não tem relação com a classe
`Aluno`, mas é um teste da função `idade` do módulo `idade`. O problema de
lidar com idade é que é um conceito relativo: uma pessoa tem uma determinada
idade em um determinado momento. Em testes automatizados, esse tipo de
relatividade temporal cria dificuldades. Neste exemplo fizemos um monkeypatch
substituindo a função `idade` por outra que sempre calcula a idade considerando
que "hoje" é uma data fixa. Isso permite que o teste funcione hoje, amanhã e
depois. O truque é feito na função `test`.

2.4. Para fazer o teste (3) passar, implemente uma property simples, apenas para leitura, com o nome `idade`. Use a função `idade.idade` e a data de nascimento do `Aluno`.

2.5. **Bônus**: Copie o arquivo `aluno.py` para `aluno2.py` e refaça o exercício
neste novo arquivo usando descriptors em vez de properties. Como o descriptor 
`Idade` depende de uma data de nascimento para funcionar, seu construtor deve 
receber o nome de um atributo do tipo `datetime.date` que será usado como 
referência para calcular a idade. Por exemplo::

    class Aluno(object):
        nascimento = Data()
        idade = Idade('nascimento')

**Dica:** Para relembrar como fazer um descriptor, veja os slides 11 a 13 da apresentação *PPQSP Turma 1, Aula 3* (`ppqsp_t1a3.pdf`_), bem como o exemplo `descr_quantidade.py`_.

.. _descr_quantidade.py: https://github.com/oturing/ppqsp/blob/master/atributos/descr_quantidade.py

3. Imitação de objetos JavaScript
==================================

Neste exercício o objetivo é criar uma classe que imita o comportamento
de objetos JavaScript, cujos atributos podem ser acessados via ``.`` ou ``[]``. Em Python, isso pode ser feito através de sobrecarga de operadores.

Por exemplo::

    >>> contato = JSObj(nome='Fred', fone='4321-1234')
    >>> contato.nome
    'Fred'
    >>> contato['fone']
    '4321-1234'

Uma vantagem de imitar o comportamento de um `dict` é aproveitar melhor o
operador de formatação de strings `%`::

    >>> '%(nome)s: %(fone)s' % contato
    'Fred: 4321-1234'

Vale notar que este comportamento do JavaScript é prático em certos casos, 
mas também cria alguns transtornos. Por exemplo, quando queremos usar um
objeto como um dicionário, é trabalhoso percorrer os itens com `for/in` porque 
recebemos de volta os métodos e até os atributos herdados, misturados com os 
dados do próprio objeto. 

Python nos dá mais flexibilidade ao permitir tratar os acessos via ``.`` ou 
``[]`` de forma bem separada. Nos casos em que a convenção do JavaScript é
mais conveniente, podemos facilmente implementá-la em Python, como este 
exercício demonstra.

3.1. Baixe o arquivo `jsobject.py`_ e o execute como um script. O resultado inicial é::

    $ python jsobject.py
    **********************************************************************
    File "jsobject.py", line 17, in __main__
    Failed example:
        o['num']
    Exception raised:
        Traceback (most recent call last):
          File "/usr/lib/python2.7/doctest.py", line 1254, in __run
            compileflags, 1) in test.globs
          File "<doctest __main__[3]>", line 1, in <module>
            o['num']
        TypeError: 'JSObj' object is not subscriptable
    **********************************************************************
    1 items had failures:
      12 of  15 in __main__
    ***Test Failed*** 12 failures.

.. _jsobject.py: https://github.com/oturing/ppqsp/blob/master/atributos/exercicios/jsobject.py

3.2. Observe que o relatório indica que aconteceram 12 falhas, mas apenas
uma está sendo exibida em detalhes, graças ao uso da opção ``doctest.REPORT_ONLY_FIRST_FAILURE``. Para fazer o teste (2) passar, basta implementar um método `__getitem__` que recebe uma string e devolve um atributo do objeto que tenha este nome. **Dica:** há duas formas de fazer isto: usar a função primitiva ``getattr(self, nome)`` ou acessar o dicionário que Python usa para armazenar os atributos de uma instância, via ``self.__dict__[nome]``. É recomendável sempre que possível evitar o acesso direto ao `__dict__`, porque isso subverte alguns mecanismos de controle de acesso a atributos e pode gerar bugs sutis. Porém, ao longo deste exercício você vai perceber que em vários momentos usar o `__dict__` é um atalho irresistível.

3.3. Para passar teste (3) basta implementar um `__setitem__` muito simples. Faça isso primeiro, verifique se o teste passa mesmo, e só depois implemente a condição exigida pelo teste (4).

3.4. O teste (5) é trivial: faça um método `__len__`. O (6) pode ser feito de várias formas. Note que até agora tudo funcionou sem que fosse preciso um `__init__` mas agora chegou o momento de implementá-lo. **Dica:** o método `dict.update` é uma ótima ferramenta para esta situação, se você optar por manipular o `__dict__` da instância diretamente.

3.5. Para fazer o (7) é preciso melhorar o `__init__`. **Dica:** novamente o `dict.update` pode ser muito útil.

3.6. A representação de um objeto em Python é usada pelo console interativo para mostrar fielmente o objeto em questão::

    >>> a = 'avião'
    >>> a
    'avi\xc3\xa3o'
    >>> s = set([3,2,4])
    >>> s
    set([2, 3, 4])
    >>>

Esta representação pode ser obtida via função `repr(o)`, que por sua vez invoca o método `o.__repr__()`. Passar pelo teste (8) envolve implementar um `__repr__`.

3.7. O teste (9) é outro exemplo de sobrecarga de operador, neste caso, ``==``. Para fazer o ``==`` funcionar é preciso implementar o método ``__eq__(self, outro)`` que deve comparar a instância com o argumento `outro` e devolver um booleano. **Dica:** comparar os `__dict__` é a saída mais fácil.

3.8. **Bônus:** Copie o arquivo `jsobject.py` para `jsobject2.py` e refaça
o exercício neste novo arquivo evitando ao máximo o acesso direto a `__dict__`
da instância. É possível fazer todos os testes passarem sem acessar nenhuma
vez o `__dict__` diretamente? 

**Nota:** Qualquer que seja a sua solução, estará 
acessando o `__dict__` indiretamente, pois ele é usado pelo próprio 
interpretador Python para todas as classes da metaclasse ``type``. A
questão é evitar o acesso direto, ou seja, não escrever `__dict__` no
seu código. Assim você torna a sua implementação mais independente da
implementação interna da classe.

----

Conclusão
==========

Este conjunto de exercícios trabalha principalmente com manipulação de
atributos, propriedades e descritores; APIs fundamentais do Python, como `len`
e `repr`, e  sobrecarga de operadores comuns, como ``.``, ``[]`` e ``==``. Se você
concluir com sucesso esta lista, terá dominado alguns dos recursos avançados
mais importantes e úteis da linguagem Python.

**Bom trabalho e Feliz Ano Novo!**

Qualquer dúvida, nos falamos pelo grupo `OTuring`_!

.. _OTuring: http://groups.google.com/group/oturing

*Luciano Ramalho*

----

© 2011, Luciano Ramalho


