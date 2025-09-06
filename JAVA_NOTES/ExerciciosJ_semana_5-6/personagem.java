public class personagem {
    
    public String nome;
    public int habilidade;
    public int energia;
    public int sorte;
    public int destreza;
    public int inteligencia;
    public int carisma;

    public void personagemBase() {

    }

    public void ataqueBase() {
        System.out.println("Eu sou um personagem e dou um soco causando 1d2 de dano.");
    }
}