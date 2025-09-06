public class main {

    public static void main(String[] args){

        mago mago = new mago();
        mago.nome = "Finócio";
        mago.habilidade = 24;
        mago.inteligencia = 34;
        mago.energia = 18;
        mago.ataqueBase();
        


        ladino ladino = new ladino();
        ladino.nome = "Angus";
        ladino.energia = 15;
        ladino.habilidade = 26;
        ladino.sorte = 16;
        ladino.sangramento = true;
        ladino.destreza = 32;
        ladino.ataqueBase();
        

        personagem bardo = new personagem();
        bardo.carisma = 28;
        bardo.energia = 9;
        bardo.sorte = 20;
        bardo.nome = "Joselito";
        bardo.ataqueBase();
        

    }
    
}
