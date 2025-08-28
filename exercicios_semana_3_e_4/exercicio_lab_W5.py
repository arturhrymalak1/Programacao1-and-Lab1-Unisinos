i = 0 
g = 0 

while True: 
    time = input("Para qual time voce torce? ")
    i += 1
    
    if time.upper() == "GREMIO": 
        g += 1 
    elif i == 10: 
        break 

print(f"Tem {g} gremistas entre voces!" )