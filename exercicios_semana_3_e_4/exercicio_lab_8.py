menu = print("""
    ================Menu================
    [1] - somar os dois valores
    
    [2] - subtrair dois valores
    
    [3] - multiplicar dois valores
    
    [4] - dividir dois valores
    
    [5] - potencia entre dois valores
    
    [6] - radiciação entre dois valores
    
    [ ] - Digite qualque coisa para sair
    
    ====================================
            """)

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

while True:
    op = input(menu)
    
    if op == 1:
        print(f"A soma dos valores inseridos é: {n1 + n2}")
    elif op == 2:
        print(f"A subtração dos valores inseridos é: {n1 - n2}")
    elif op == 3:
        print(f"A multiplicação dos valores inseridos é: {n1 * n2}")
    elif op == 4:
        print(f"A divisão dos valores inseridos é: {n1 / n2}")
    elif op == 4:
        print(f"A sradiciação dos valores inseridos é: {n1 ** (1/n2)}")
    elif op == 4:
        print(f"A potencia dos valores inseridos é: {n1 ** n2}")
    else:
        break