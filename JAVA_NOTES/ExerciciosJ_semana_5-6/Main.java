public class Main {

    public static void main(String[] args){

    Empregado artur = new Empregado("Artur Llantada");
    artur.setTurno('N');
    artur.setSalario(2500);
    artur.calculaAdicionalNoturno();
    artur.aumentaSalario(500);

    artur.imprimeInformacoes();

    }
}