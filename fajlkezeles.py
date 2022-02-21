f=open("adatok.txt")
f2=open("adatoksorszam.txt","w")

sorszam=1
for egysor in f:
    f2.write(str.sorszam+" "egysor)
    sorszam=1
    
