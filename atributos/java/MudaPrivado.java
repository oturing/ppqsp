import java.lang.reflect.Field;

public class MudaPrivado {

	public static void main(String[] args) {
		ObjetoSecreto oSecreto = new ObjetoSecreto("nada");
		Field campoPrivado = null;
		try {
			campoPrivado = ObjetoSecreto.class.getDeclaredField("oculto");
		}
		catch (NoSuchFieldException e) {
			System.err.println(e);
			System.exit(1);
		}
		campoPrivado.setAccessible(true); // arrombamos a porta
		try {
			String tavaEscondido = (String) campoPrivado.get(oSecreto);
			System.out.println("oSecreto.oculto = " + tavaEscondido);
			campoPrivado.set(oSecreto, "novo segredo");
			tavaEscondido = (String) campoPrivado.get(oSecreto);
			System.out.println("oSecreto.oculto = " + tavaEscondido);
		}
		catch (IllegalAccessException e) { 
			// esta exceção nao acontece porque fizemos setAcessible(true)
			System.err.println(e);
		}	
	}
}
