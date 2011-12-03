import ObjetoSecreto

oSecreto = ObjetoSecreto('nada')
campoPrivado = ObjetoSecreto.getDeclaredField('oculto')
campoPrivado.setAccessible(True) # arrombamos a porta
print 'oSecreto.oculto =', campoPrivado.get(oSecreto)
campoPrivado.set(oSecreto, 'novo segredo')
print 'oSecreto.oculto =', campoPrivado.get(oSecreto)
