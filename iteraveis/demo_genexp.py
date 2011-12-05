from time import sleep, strftime
import sys

verboso = len(sys.argv) == 2 and sys.argv[1] == '-v'

def demora(ts=1):
    agora = strftime('%H:%M:%S')
    print 'demorando...', agora
    sleep(1)
    return agora

if verboso:
    print 'Teste com list comprehension [listcomp]'
    print '  repare como todas as demoras acontecem primeiro,'
    print '  depois o resultado aparece todo de repente.'
raw_input('(tecle <ENTER> para rodar o teste LISTCOMP) ')

for t in [demora() for i in range(3)]:
    print t

if verboso:
    print
    print 'Teste com expressao geradora (genexp)'
    print '  repare que acontece uma demora e aparece um resultado,'
    print '  depois outra demora e outro resultado, ate o fim'
raw_input('(tecle <ENTER> para rodar o teste GENEXP) ')

for t in (demora() for i in range(3)):
    print t
