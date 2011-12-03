import java.lang.reflect.Field;

public class Teste {

	public static void main(String[] args) {
		ObjetoSecreto oSecreto = new ObjetoSecreto("senha super secreta");
		String tavaEscondido = null;
		Field campoPrivado = null;
		try {
			campoPrivado = ObjetoSecreto.class.getDeclaredField("escondido");
		}
		catch (NoSuchFieldException e) {
			System.err.println(e);
			System.exit(1);
		}
		campoPrivado.setAccessible(true); // arrombamos a porta
		try {
			tavaEscondido = (String) campoPrivado.get(oSecreto);
		}
		catch (IllegalAccessException e) { 
			// esta exceção nao acontece porque fizemos setAcessible(true)
			System.err.println(e);
			System.exit(1);
		}	
		System.out.println("oSecreto.escondido = " + tavaEscondido);
	}
}
