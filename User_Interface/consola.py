from Domain.rezervari import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from User_Interface.meniu import meniu, meniu_CRUD

def ui_adauga_rezervare(lista):
    ID = input('Dati ID-ul rezervarii: ')
    nume = input('Dati numele: ')
    clasa=input('Clasa: ')
    pret= input ('Dati pretul: ')
    checkin_facut = input('Checkin: ')
    try:
        rezervare = adauga_rezervare( ID, nume, clasa, pret, checkin_facut,lista)
        print('Rezervarea a fost adaugata cu succes')
        return rezervare
    except ValueError as ve:
        print("au aparut erori",ve)


def ui_sterge_rezervare(lista):
    ID = int(input('Dati ID-ul rezervarii de sters: '))
    return sterge_rezervare(ID, lista)


def ui_modifica_rezervare(lista):
    ID = input('Dati ID-ul rezervarii de modificat: ')
    nume = input('Dati noul nume: ')
    clasa=input('Noua clasa: ')
    pret= input ('Dati noul pret: ')
    checkin_facut = input('Checkin: ')
    try:
        rezervare= modifica_rezervare(ID, nume, clasa, pret , checkin_facut, lista)
        print("Rezervarea a fost modificata cu succes!")
        return rezervare
    except ValueError as ve:
        print("au aparut erori",ve)
    except:
        print("unknown error")



def show(lista):
    for rezervare in lista:
        print(to_string(rezervare))

def consola(lista):
    while True:
        meniu()
        optiune = input('Dati optiunea: ')

        if optiune == '1':
            while True:
                meniu_CRUD()
                cmd = input('Dati optiunea: ')
                if cmd=='1':
                    lista = ui_adauga_rezervare(lista)
                elif cmd=='2':
                    lista=ui_sterge_rezervare(lista)
                elif cmd=='3':
                    lista=ui_modifica_rezervare(lista)
                elif cmd == 'a':
                    show (lista)
                elif cmd == 'x':
                    break
                else:
                    print('Optiune gresita! Reincercati: ')
        elif optiune=='2':
            pass
        elif optiune == '3':
            pass
        elif optiune == '4':
            pass
        elif optiune == '5':
            pass
        elif optiune=='6':
            pass
        elif optiune == '7':
            pass
