vogal = ["a", "e", "i", "o", "u"]

ltr = input("Digite uma letra qualquer: ").lower()

if ltr in vogal:
    letra = "vogal"
else:
    letra = "consoante"

print(f"A letra digitada é {letra}")