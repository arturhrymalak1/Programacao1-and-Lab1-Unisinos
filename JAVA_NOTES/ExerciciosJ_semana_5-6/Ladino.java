public class Ladino{
    
    public String nome;
    public int habilidade;
    public int energia;
    public int sorte;
    public int destreza;

    public void backStab(){
        System.out.println("Back Stab");
    }

    @Override
    public String toString() {
        return "Ladino\nNome: " + nome + "\nHabilidades: ";
    }

    
}