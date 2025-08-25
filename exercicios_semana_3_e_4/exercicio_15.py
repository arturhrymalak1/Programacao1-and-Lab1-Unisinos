compras = []

j = int(input("Quantos itens tu vais comprar? "))

for i in range(0, j):
    compras.append(input("\nAdicionar item: "))

print("\nAqui está sua lista de compras\n")
for i in compras:
    print(i)