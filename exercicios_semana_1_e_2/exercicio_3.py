#Solicite o nome do usuário depois imprima na tela, em seguida faça o mesmo com a altura,
#depois manda uma mensagem de agradecimento.

import time

nome = input("Qual teu nome? ")

print(f"Olá {nome}!!")

altura = float(input("Qual sua altura? "))

print(f"Sua altura é {altura:.2f}")

time.sleep(2)

print(f"Muito obrigado {nome} por responder as perguntas!!")