import sys
import atexit

print '-> 1 inicio'

def funcaoA():
    print '-> 2 funcao A'
    return 'resultado A'

def funcaoB():
    print '-> 3 funcao B'

    def funcaoC():
        print '-> 4 funcao C'

    return funcaoC

funcaoD = lambda:sys.stdout.write('-> 5 funcao D\n')

def funcaoE():
    print '-> 6 funcao E'

def funcaoF():
    print '-> 7 funcao F'

class Classe(object):
    print '-> 8 bloco de declaracoes da Classe'

    def __init__(self):
        print '-> 9 inicializacao da instancia da Classe'

    def metodo(self, default=funcaoF()):
        print '-> 10 metodo da instancia da Classe'
        return 'resultado metodo'

    class ClasseInterna(object):
        print '-> 11 bloco de declaracoes da ClasseInterna'

    def __del__(self):
        print '-> 12 destruicao da instancia da Classe'

if True:
    print '-> 13 condicional True'

if False:
    assert False, 'Isso nunca devia acontecer'

atexit.register(funcaoE)

print '-> 14 logo antes do if __main__'

if __name__=='__main__':
    print '-> 15 __main__'
    print funcaoA
    print funcaoA()
    print '-> 16 __main__ (cont.)'
    print funcaoB
    resultadoB = funcaoB()
    print resultadoB
    objeto = Classe()
    objeto.metodo()
    resultadoB()
    print funcaoD
    funcaoD()
    class Local(object):
        print '-> 17 bloco de declaracoes da classe Local'
    print '-> 18 __main__ (final)'
print '-> 19 FIM'
