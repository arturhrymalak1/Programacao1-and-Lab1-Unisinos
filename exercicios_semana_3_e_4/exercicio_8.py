import time

def contarAte(a):
    while True:
        print(a)
        a += 1
        if a == 1001:
            break

b = contarAte(0)

print(b)