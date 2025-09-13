public class Main {

    public static void main(String[] args){

    Livro livro1 = new Livro();
        livro1.setTitulo("A volta dos que não foram");
        livro1.setAutor("Antedeguemon");
        livro1.setAnoPublicacao(1945);
        livro1.setPreco(696.90);
        livro1.setQutPag(969);

    
    livro1.toString();
    livro1.precoPag(livro1.getQutPag(), livro1.getPreco());

    Livro livro2 = new Livro();
        livro2.setTitulo("As lindas Tranças de um Careca");
        livro2.setAutor("Manoel Gomes");
        livro2.setAnoPublicacao(2028);
        livro2.setPreco(86.63);
        livro2.setQutPag(80);
    
    livro2.toString();
    livro2.precoPag(livro2.getQutPag(), livro2.getPreco());

    Livro livro3 = new Livro();
        livro3.setTitulo("Ostenis gastos de um cadeirante");
        livro3.setAutor("Leo Lins");
        livro3.setAnoPublicacao(2500);
        livro3.setPreco(4.67);
        livro3.setQutPag(3);
        
    livro3.toString();
    livro3.precoPag(livro3.getQutPag(), livro3.getPreco());

    Cliente cliente1 = new Cliente();
        cliente1.setNome("Artur");
        cliente1.setIdade(18);
        cliente1.setSexo('M');
        cliente1.setEmail("shaolinmatadordeporco24@gmail.com");
        cliente1.setSenha("123@senha");

    }
}