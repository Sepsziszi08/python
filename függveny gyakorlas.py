'''
def negyzet(a):
    return a**2

q=negyzet(10)
print(q)
print(negyzet(8))

osszeg=0
for i in range (10):
    osszeg+=negyzet(i+1)

print(osszeg)
'''

#Köszönés

import random
def koszon(nev):
    koszonesek=("Szevasz","Csá","Anyád","Hello","Szia","Baktalo","Rohadjál meg")
    print(random.choice(koszonesek),nev)

    
koszonCount=0
def koszon2(nev="Kedves barátom"):
    koszonesek=("Szevasz","Csá","Anyád","Hello","Szia","Baktalo","Rohadjál meg")
    print(random.choice(koszonesek),nev)



koszon("Józsi")
koszon("Béla")
koszon("Pali")
koszon("Karcsi")
koszon("Gyula")
koszon("Norbi")
koszon("Péter")
