
"""
be=input ("Kérek egy kisbetűt:")
print(be.upper())


be=input ("Kérek egy nagybetűt:")
print(be.lower())


for i in range(70):
    print (be, end="")

print()
print(be.ljust(70,be))


be=input("Kérek egy szöveget:")
if len(be)>=12:
    if be[11]=="k":
        print("igaz")
    else:
        print("nem igaz")



print(be[0:3])
print (be[-3:])
szo=be[0:3].upper()+be[3:-3].lower()+be[-3:0].upper()
print(szo)
"""

#Kérjünk be egy mondatot és a modat szavait fordítva írja ki.
"""
be=input ("Kérek egy mondatot! ")
fordit=be.split(" ")
print(fordit)
fordit.reverse()
print (fordit)
print(" ".join(fordit).capitalize)
"""

be="Kérjen be egy számot és számolja meg hány és van benne."
darab=be.replace(",""").split(" ")
db=0
for szo in darab:
    if szo=="és":
        db+=1
if db==0:
    print("Nem volt egy sem")
else:
    print(str(db)+" darab volt.")

print (" "+be.replace(",""")+" ").count(" és "))
