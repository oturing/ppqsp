from random import randint

def dado():
    return randint(1,6)

# gera valores ate que um 6 seja sorteado
for r in iter(dado, 6): # 6 e' o "sentinela"
    print r
