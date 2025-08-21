print("Verificador e ano bisexto\n")

while True:
    ano = int(input("digite um ano para saber se ele é ou foi bisexto: "))

    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"O ano de {ano} é ou foi Bisexto!!")
        else:
            print(f"O ano de {ano} não é ou foi Bisexto!!")
    elif ano % 4 == 0:
        print("O ano é Bisexto!!")
    else:
        print("O ano não é Bisexto!")

    op = input("Deseja continuar pesquisando?(s/n) ")
    if op == "n":
        break