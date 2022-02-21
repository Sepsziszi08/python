#f=open("proba.txt","w")
#f.write("picsku")
#f.close()

def file_kiir(file_nev):
    f=open(file_nev)
    print(f.read())
    
f.close()

f=open("adatok.txt","w")

be="baktalo"
while be!="":
    be=input("Sorosterv! ")
    if be!="":
        f.write(be+"\n")
        

f.colse()

file_kiir("adatok.txt")
