def verificaMeno(a, b):
    if a < b:
        s = b - a
    else:
        s = a - b
    return s



val1 = int(input("Digite um numero: "))
val2 = int(input("Digite outro numero: "))


if val1 < 0 or val2 < 0:
    while i < verificaMeno(val1, val2):
        print()
        i += 1
        