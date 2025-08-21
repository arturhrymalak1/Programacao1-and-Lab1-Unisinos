disc = input("Qual Discciplina vc deseja calcular tua nota? ")

gA = float(input("Qual sua nota no Grau A? "))

gB = float(input("Qual sua nota no Grau B? "))

ga = gA * 0.3

gb = gB * 0.7

if ga < 0 or gb < 0:
    print("Erro! A nota não pode ser negativa!!")
elif ga + gb <= 5:
    print("Vai ter que fazer o Grau C irmão!")
else:
    print(f"Parabéns irmão, Você passou na Disciplina de {disc} com média {ga + gb :.2}")