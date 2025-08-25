import time

n1 = int(input("digite um numero para saber a tabuada do mesmo: "))

for i in range(0, 10):
    i += 1
    time.sleep(0.07)
    print(f"{i} x {n1} = ",i * n1)