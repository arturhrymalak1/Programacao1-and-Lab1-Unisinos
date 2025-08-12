print("\nHoje vamos resolver uma equação de segundo grau!!\n Parecida com essa - ax² + bx + c = 0")

a = int(input("Insira um valor inteiro para a: "))

b = int(input("Insira um valor inteiro para b: "))

c = int(input("Insira um valor inteiro para c: "))

x1 = (- b + ((b**2) - (4 * a * c))**(1/2)) / (2*a)

x2 = (- b - ((b**2) - (4 * a * c))**(1/2)) / (2*a)

print(f"x' (raiz positiva) é iagual a  {x1:.2f}\nJá x'' (raiz negativa) é iagual a {x2:.2f}")