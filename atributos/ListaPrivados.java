import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

public class ListaPrivados {

	public static void main(String[] args) {
		ObjetoSecreto oSecreto = new ObjetoSecreto("senha super secreta");
		Field campos[] = ObjetoSecreto.class.getDeclaredFields();
		for (Field campo : campos)
			if (Modifier.isPrivate(campo.getModifiers())) { // só campos privados!
				System.out.println(campo.toString());
				campo.setAccessible(true); // arrombamos a porta
				try {
					String valor = (String) campo.get(oSecreto);
					System.out.println("\t" + campo.getName() + " -> " + valor);
				}
				catch (IllegalAccessException e) { 
					// esta exceção nao acontece porque fizemos setAcessible(true)
					System.err.println(e);
					System.exit(1);
				}	
			}
	}
}
