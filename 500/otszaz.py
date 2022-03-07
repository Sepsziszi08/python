def ertek(darab):
    if darab=1:
        return 500
    else:
        return darab*400+150




f=open("penztar.txt")
kosar=[]
#szoveg=f.read()
#print(szoveg)
for sor in f:
    kosar.append(sor.strip())
f.close()

print("2. feladat")
print("Fizetések száma: " + str(kosar.count("F")))


print("3. feladat")
print("Az első vásárló " + str(kosar.index("F")) + " darab árucikket vásárlolt.")


sorszam=int(input("Vásárlás sorszáma: "))
arunev=input("Árucikk neve: ")
darab=int(input("Darabszám: "))

aruindex=kosar.index(arunev)
darablista=kosar[:aruindex]
#print(darablista)
vasarlasdb=darablista.count("F") +1

#print("5. feladat")
print("Az első vásárlás sorszáma: " +str(vasarlasdb))

utolsoindex=0
for i in range  (0,len(kosar)):
      if kosar[i*-1-1]==arunev:
          utolsoindex=len(kosar)-i
          break
darablista=kosar[:utolsoindex]
vasarlasdb=darablista.count("F") + 1
print("AZ utolsó vásárlás sorszáma: " + str(vasarlasdb))
        
voltf=False
szam=0
for e in kosar:
    if e =arunev:
        if not voltf:
            szam=szam+1
            voltf=True
    if e=="F":
        voltf=False
print(str(szam)+" vásárlás során vettek belőle. ")

print("6. feladat")
print(str(vasarlasdb)+ " darab vételekor fizetendő: "+ str(ertek(vasarlasdb)))

darabf=0
elozoindex=0
keresettindex=0
for i in range (0:len(kosar)):
    if kosar[i]=="F":
        darabf+=1
    if darabf=sorszam
        elozoindex=keresettindex
        keresettindex=i
        break
    





