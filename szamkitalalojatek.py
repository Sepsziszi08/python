import random
import math
import os
import sys

def Alexajateka():

    lower = int(input("Írd be az alsó számhatárt:- "))
     

    upper = int(input("írd be a felső számhatárt:- "))
     

    x = random.randint(lower, upper)
    print("\n\t",
           round(math.log(upper - lower + 1, 2)),
          " lehetőséged van tippelni.\n")
     

    count = 0
     

    while count < math.log(upper - lower + 1, 2):
        count += 1
     
        guess = int(input("Írj be egy számot:- "))
     
        if x == guess:
            
            print("Gratulálok, kitaláltad a(z)",
                  count,". próbálkozásra!")

            break
        elif x > guess:
            print("Kisebb számra tippeltél.")
        elif x < guess:
            print("Nagyobb számra tippeltél.")
     

    if count >= math.log(upper - lower + 1, 2):
        print(" \n\t A szám a(z) %d volt.\n" % x)




    result=input("\n Újraszeretnéd kezdeni? [y/n] > ")
    if result=='y':
         os.system('python "C:/Users/dudasa20/Desktop/szamkitalalojatek.py"')
    else:
         print("\nViszlát")
