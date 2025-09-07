import java.util.Scanner;

public class main {

    public static void main(String[] args){
        
        Scanner scan = new Scanner(System.in);

        mago mago = new mago();
        System.out.println("Digite o nome do Mago: ");
        mago.setNome(scan.nextLine());
        System.out.println(mago.getNome());

        ladino ladino = new ladino();
        
        ladino.ataqueBase();
        

        personagem bardo = new personagem();
    
        bardo.ataqueBase();
        

    }
    
}
