public class ladino extends personagem{
    
    boolean sangramento;

    public void ladinoHabilidades(){
        System.out.println("Habilidade: BackStab[+1d4] mais sangramento caso for cítico.");
    }

    @Override
    public void ataqueBase() {
        if (sangramento == true) {
            System.out.println("Eu sou um ladino e dou 1d4 de dano a mais para sangramento");
        }else{
            System.out.println("eu sou um ladino e dou apena um 1d4 somente");
        }
    }
}
