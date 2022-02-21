f=open("autok.txt")
teljes=f.read()
#print(teljes)
f.close()
teljes=teljes[0:-1]

darabok=teljes.split("\n")
print(darabok)

for egysor in darabok:
    vag=egysor.split(" ")
    print(vag[2])
