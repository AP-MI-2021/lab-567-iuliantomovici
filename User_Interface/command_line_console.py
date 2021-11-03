from Domain.rezervari import to_string
from Logic.CRUD import *



def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def consola_noua(lista):

    while True:
        mesaj=input('introduceti comanda: ')
        if mesaj=="help":
            print("Add ID nume clasa pret checkin facut -> adauga rezervare")
            print("Delete id -> sterge rezervare")
            print("Update id nume clasa pret checkin facut -> modifica rezervare")
            print("Showall -> afiseaza toate rezervarile")
            print("Exit -> opreste programul")
        else:
            comanda=mesaj.split(",")
            for i in range(len(comanda)):
                optiuni=comanda[i].split(" ")
                if optiuni[0]=="Exit":
                    break
                elif optiuni[0]=="Add":
                    try:
                        lista= adauga_rezervare(optiuni[1], optiuni[2], optiuni[3], optiuni[4], optiuni[5], lista)
                    except ValueError as ve:
                        print("Eroare : {}".format(ve))
                elif optiuni[0] == "Showall":
                    show_all(lista)
                elif optiuni[0] == "Update":
                    lista = modifica_rezervare(optiuni[1], optiuni[2], optiuni[3], optiuni[4], optiuni[5], lista)
                elif optiuni[0] == "Delete":
                    try:
                        lista = sterge_rezervare(optiuni[1], lista)
                    except ValueError as ve1:
                        print("Eroare : {}".format(ve1))
                else:
                    print("Optiune gresita! Acceseaza comanda 'help'!")

