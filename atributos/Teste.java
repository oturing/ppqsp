public class Teste {

    public static void main(String[] args) {

        ObjetoSecreto oSecreto = new ObjetoSecreto("senha super segura");

        Field campoPrivado = ObjetoSecreto.class.getDeclaredField("segredo");

        campoPrivado.setAccessible(true); // arrombamos a porta

        String eraSegredo = (String) privateStringField.get(privateObject);
        System.out.println("oSecreto.segredo = " + eraSegredo);
    }
}
