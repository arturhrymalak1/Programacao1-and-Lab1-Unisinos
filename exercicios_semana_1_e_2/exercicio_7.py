# Uma determinada disciplina possui apenas 3 avaliações: o
# trabalho (que vale 10% da nota), a prova (que vale 60% da
# nota) e o teste (que vale 30% da nota).

# Crie um programa que pede para o usuário digitar as notas
# que ele tirou nestas avaliações e imprime na tela a nota final do
# aluno.

nota1 = float(input("Digite a nota tirada no trabalho: "))
nota2 = float(input("Digite a nota tirada na prova: "))
nota3 = float(input("Digite a nota tirada no teste: "))

media_final = (nota1 * 0.10) + (nota2 * 0.60) + (nota3 * 0.30)

print(f"Sua nota final foi de {media_final :.2f}")