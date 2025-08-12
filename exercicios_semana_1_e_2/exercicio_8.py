# Uma disciplina possui Grau A e Grau B. A nota do Grau A vale
# 33% da nota final, enquanto a nota do Grau B vale 67% da
# nota final. O Grau A possui as seguintes avaliações:
# - Atividade prática: 45% da nota do Grau A
# - Atividade teórica: 55% da nota do Grau A

# Já o Grau B possui as seguintes avaliações:
# - Prova em laboratório: 60% da nota do Grau B
# - Teste teórico: 20% da nota do Grau B
# - Trabalho extraclasse: 20% da nota do Grau B

# Crie um programa que solicite as notas de todas as avaliações e
# imprime na tela a nota final obtida na disciplina.

pratica_a = float(input("Qual sua nota da atividade pratica? "))

teorica_a = float(input("Qual sua nota da atividade teórica? "))

finalga = (pratica_a * 0.45) + (teorica_a * 0.55)

prolab_b = float(input("Qual sua nota da prova de lab? "))

teorica_b = float(input("Qual sua nota do teste teórico? "))

trabex_b = float(input("Qual sua nota do trabalho extra classe? "))

finalgb = (prolab_b * 0.60) + (teorica_b * 0.20) + (trabex_b * 0.20)

print(f"A média final da Disciplina foi {(finalga + finalgb) / 2}")