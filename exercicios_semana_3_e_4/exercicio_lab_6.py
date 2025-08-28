valor = float(input("Digie o valor que voce vai pagar para calcular o juros: "))

if valor < 100:
    print(f"Você vai pagar R$ {valor * 0.10:.2f} de juros.")
    print(f"\nO valor a pagar é de R$ {valor * 1.10:.2f}")
elif valor >= 100 and valor < 300:
    print(f"Você vai pagar R$ {valor * 0.30:.2f} de juros.")
    print(f"\nO valor a pagar é de R$ {valor * 1.30:.2f}")
elif valor >= 300 and valor < 1000:
    print(f"Você vai pagar R$ {valor * 0.50:.2f} de juros.")
    print(f"\nO valor a pagar é de R$ {valor * 1.50:.2f}")
elif valor < 0:
    print("ERRO: O valor digitado é negativo!")
else:
    print("Valor inválido")