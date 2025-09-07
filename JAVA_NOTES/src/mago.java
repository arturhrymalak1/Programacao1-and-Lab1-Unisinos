public class mago extends personagem{
    
    String fireball = "Fire Ball";

    public void fireBall(){
        System.out.println("Magias: " + fireball + "[1d8]");
    }

    @Override
    public void ataqueBase(){
        System.out.println("eu sou um mago e dou 1d8 de dano com minha magia");
    }
}
