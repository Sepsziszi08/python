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
for e in kosar:if e =arunev:
