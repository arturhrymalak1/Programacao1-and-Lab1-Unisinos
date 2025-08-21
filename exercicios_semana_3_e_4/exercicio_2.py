print("Vamos fazer uma divião?\n")
while True:
    nu = float(input("\nInforme o Dividendo: "))
    nd = float(input("Informe o Divisor: "))

    if nd == 0:
        print("ERRO: O VALOR DO DIVISOR NÃO PODE SER 0!")
    else:
        print(f"A o Resultado da Divisão é {nu/nd :.2f}")
    
    op = input("Deseja sair? (s/n) ")
    if op == "s":
        break