import java.lang.reflect.Field;
import java.lang.NoSuchFieldException;
import java.lang.IllegalAccessException;

public class Teste {

	public static void main(String[] args) {
		ObjetoSecreto oSecreto = new ObjetoSecreto("senha super secreta");
		try {
			Field campoPrivado = ObjetoSecreto.class.getDeclaredField("escondido");
			campoPrivado.setAccessible(true); // arrombamos a porta
			String tavaEscondido = (String) campoPrivado.get(oSecreto);
			System.out.println("oSecreto.escondido = " + tavaEscondido);
		}
		catch (NoSuchFieldException e) {
			System.err.println(e);
		}	
		catch (IllegalAccessException e) {
			System.err.println(e);
		}	
	}
}
