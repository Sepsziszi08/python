class beker:
    def __init__(self):
        pass
    def form(self):
        self.rendszam=input("rendszam: ")
        self.sofor=input("sofor: ")
        self.indulkm=int(input("indul:  km"))
        self.megallkm=int(input("megall: (km)"))
        self.tankol=int(input("tankolt: "))

if _name_ == "_main_":
    adat=beker()
    adat.form()
    print("megtett km: "+str(adat.megallkm-adat.indulkm))
else:
    print("Ez egy modul")

