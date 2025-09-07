public class lampada {
    boolean ligada;

    public void lampadaLigada(boolean ligada) {
        this.ligada = ligada;
        if (ligada == true){
            System.out.println("a lampada está ligada!");
        }else{
            System.out.println("a lampada está desligada!");
        }
    }
}