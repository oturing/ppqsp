from random import randint
from functools import partial

# exibe valores ate que um 6 seja sorteado
# 6 e' o "sentinela"
for r in iter(partial(randint,1,6), 6):
    print r
