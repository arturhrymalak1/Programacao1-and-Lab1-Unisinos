public class Livro {
    private String titulo;
    private String autor;
    private int anoPublicacao;
    private double preco;
    private int qutPag;

    public void livro(String titulo, String autor, int anoPublicacao, double preco, int qutPag){
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.preco = preco;
        this.qutPag = qutPag;
    }

    public double precoPag(int qutPag, double preco){
        return (qutPag * preco);
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public void setAnoPublicacao(int anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public int getQutPag() {
        return qutPag;
    }

    public void setQutPag(int qutPag) {
        this.qutPag = qutPag;
    }

    @Override
    public String toString() {
        return "\nInformações do Livro:\nTitulo: " + titulo + 
        "\nAutor: " + autor + 
        "\nAno de Publicação: " + anoPublicacao + 
        "\nQauntidade de páginas: " + qutPag + 
        "\nPreço: " + preco;
    }
    

}