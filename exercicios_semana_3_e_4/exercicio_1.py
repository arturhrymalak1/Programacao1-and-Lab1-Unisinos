while True:
    n1 = int(input("\nInforme um numero: "))

    if n1 % 3 == 0:
        print("O nuemro é impar!")
    elif n1 % 2 == 0:
        print("O numero é par!")
    elif n1  == 0:
        print("ERRO: numero é zero!")
    elif n1 < 0:
        print("ERRO: numero é negativo!")
    else:
        print("ero")
    
    op = input("Deseja Sair? (s/n) ")
    if op == "s":
        break
