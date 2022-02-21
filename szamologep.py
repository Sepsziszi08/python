def Olijateka():

    def szamolas():

        print("1:Összeadás")
        print("2:Kivonás")
        print("3:Szorzás")
        print("4:Osztás")

        muvelet=int(input("Kérem a művelet számát: "))

        szam1=int(input("Kérem az első számot: "))
        szam2=int(input("Kérem a második számot: "))

        if muvelet == 0:
            print(szam1+szam2)
        elif muvelet == 1:
            print(szam1-szam2)
        elif muvelet == 2:
            print(szam1*szam2)
        elif muvelet == 3:
            print(szam1/szam2)


    szamolas()

    def folytatas():
        kovetkezo=""
        while kovetkezo!="igen" and kovetkezo!="nem":
            kovetkezo=input("Szeretnéd folytatni?: ")
        return kovetkezo

    while folytatas()=="igen":
        szamolas()
