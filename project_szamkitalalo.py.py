import random

szam = random.randint(1, 10)
tipp = None

while tipp != szam:
    tipp = input("Tippeld meg a számot 1 és 10 között: ")
    tipp = int(tipp)

    if tipp == szam:
        print("Gratulálok, eltaláltad!")
    
    elif tipp > szam:
        print("Túl nagy a tipped")
    else:  
        print("Túl kicsi a tipped!")
    
