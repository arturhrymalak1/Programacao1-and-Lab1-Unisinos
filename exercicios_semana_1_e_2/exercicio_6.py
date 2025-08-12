# Crie um programa que pede 5 números inteiros pelo
# teclado e armazena-os, respectivamente, nas variáveis
# A, B, C, D e E. Em seguida, faça o que se pede:

# - sabendo que B e C são respectivamente a base e a altura de
# um triângulo, imprima a área deste triângulo

# - sabendo que A, B, C e D formam um retângulo, imprima o
# perímetro deste retângulo

# - sabendo que E é o valor do raio de um determinado círculo,
# imprima a área deste círculo

import math

a = int(input("Insira um numero qualquer: "))
b = int(input("Insira um segundo numero qualquer: "))
c = int(input("Insira um terceiro numero qualquer: "))
d = int(input("Insira um quarto numero qualquer: "))
e = int(input("Insira um quinto numero qualquer: "))

print(f"\nSe {b} e {c} fossem respectivamente a base e altura de um triangulo a sua área seria {(b * c) / 2}.")

print(f"\nSe existisse um retangulo com as dimenções {a}, {b}, {c} e {d}, seu perimetro seria {a + b + c + d}.")

print(f"\nCaso {e} fosse o raio de um circulo, a area desse circulo seria {math.pi * e**2 :.2f}")