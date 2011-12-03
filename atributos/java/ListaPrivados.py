from java.lang.reflect import Modifier
import ObjetoSecreto

oSecreto = ObjetoSecreto('senha super secreta')
campos = ObjetoSecreto.getDeclaredFields()
for campo in campos:
	if Modifier.isPrivate(campo.getModifiers()): # so campos privados!
		print campo
		campo.setAccessible(True) # arrombamos a porta
		print '\t', campo.getName(), '=', campo.get(oSecreto)
