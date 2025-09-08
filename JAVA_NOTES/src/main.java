import java.util.Scanner;

public class main {

    public static void main(String[] args){
        
        Scanner scan = new Scanner(System.in);

        mago mago = new mago();
        System.out.println("Digite o nome do Mago: ");
        mago.setNome(scan.nextLine());  
        System.out.println("Olá "+ mago.getNome());


        ladino ladino = new ladino();
        System.out.println("Digite o seu nome ladino: ");
        ladino.setNome(scan.nextLine());
        System.out.println("Eu sou " + ladino.getNome() + " O assasino mais temido dessa rua!");
        ladino.ataqueBase();
        

        personagem bardo = new personagem();
    
        bardo.ataqueBase();
        

    }
    
}
