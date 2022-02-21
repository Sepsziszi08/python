import sys
import snake
import szamkitalalojatek
import szamologep
import tictactoe

def jatekok():
    print("""
            1: Snake
            2: Számkitaláló
            3: Számológép
            4: Tic-Tac-Toe
            5: KILÉPÉS
          """)

    jatek=input("Melyik játékkal szeretnél játszani?: ")
    if jatek=="1":
        snake.Attilajateka1()
    elif jatek=="2":
        szamkitalalojatek.Alexajateka()
    elif jatek=="3":
        szamologep.Olijateka()
    elif jatek=="4":
        tictactoe.start()
    elif jatek=="5":
        sys.exit()


def ujrakezdes():
    kovetkezo=""
    while kovetkezo!="igen" and kovetkezo!="nem":
        kovetkezo=input("Szeretnél mással játszani?: ")
    return kovetkezo

ujra="igen"

while ujra=="igen":
    jatekok()
    ujra=ujrakezdes()

