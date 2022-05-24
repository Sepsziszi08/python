import math
def vane(oszlop,ertek):
    for o in tabla:
        if o [oszlop]==ertek:
            return True
    return False


def resztabla(sor,oszlop):
    s=math.ceil((sor+1)/3)-1
    o=math.ceil((oszlop+1)/3)

    return s*3+o

    print("A hely a(z) () résztáblához tartozik. ".format(s*3+o))

    
print("1. feladat")
filenev=input("Adja meg a bemeneti fájl nevét! ")
sor=int(input("Adja meg egy sor számát! "))
oszlop=int(input("Adja meg egy oszlop számát! "))

f=open(filenev)
sorok=f.read().split("\n") [:-1]
f.close()

adatok=[]
for sor in sorok:
    adatok.append(sor.split(" "))

adatok2=[]
for sor in adatok:

    temp=[]
    for elem in sor:
        temp.append(int(elem))

    adatok2.append(temp)

#print(adatok)
#print(adatok2)

tabla=adatok[:9]
lepesek=adatok[9:]

print("3. feladat")
print("Az adott helyen szereplő szám: "+str(tabla[sor-1][oszlop-1]))
if tabla[sor-1][oszlop-1]=="0":
    print("AZ adott helyet még nem töltötték ki. ")
else:
    print("Az adott helyen szereplő szám: "+str(tabla[sor-1][oszlop-1]))

s=math.ceil(sor/3)-1
o=math.ceil(oszlop/3)

volt=False
for i in range(0,9):
    for k in range(0,9):
        if resztabla(ts,to)==resztabla(i,k):
            if tabla[i][k]==lepes[0]:
                volt=True
tabla=s*3+o
print("A hely a(z) () résztáblához tartozik. ".format(s*3+o))

db=0
for a in tabla:
    db+=s.count("0")
db=tabla.count("0")

print("4. feladat")
print("Az üres helyek aránya:  ():.0%" .format(db/811))
print(db)
ts=int(lepes[1])-1
to=int(lepes[2])-1

for lepes in lepesek:
    print(tabla[int(lepes[1])-1][int(lepes[2])-1])
    
    if tabla[ts][to]!="0":
        print ("A helyet már kitöltötték")
    elif lepes[0] in tabla[ts]:
        print("Az adott sorban már szerepel a szám")
    elif vane(to,lepes[0]):
