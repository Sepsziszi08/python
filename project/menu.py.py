import beker

menu_options = {
    1: "menüpont 1",
    2: "menüpont 2",
    3: "menüpont 3",
    4: "kilépés",
}



def print_menu():
    print(menu_options)
    for menupontindex in menu_options:
        minta="() --- ()"
        print(minta.format(menupontindex, menu_options[menupontindex]))
        #print(menu_options[menupontindex])
    pass


while (True):
    print_menu()
    try:
        option=int(input("válassz: "))
    except:
        option="rak"
        pass
    
    if ootion==1:
        print("Hozd gyorsan a baseball ütőt")
    elif option==2:
        print("Hülye vagy mint a fal, gyerek")
    elif option==3:
        print("Jól van ma nem verlek meg")
    elif option==4:
        print("Nem is vagy ze olyan hülye gyerek")

    else:
        print("Esélytelen")
    
