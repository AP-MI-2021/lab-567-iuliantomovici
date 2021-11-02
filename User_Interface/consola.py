from Domain.rezervari import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.ieftinire import ieftinire
from Logic.ordonare import ordonare, ordonare_2
from Logic.pret_maxim import *
from Logic.sume import sume
from Logic.validare import validare_procent
from User_Interface.meniu import meniu, meniu_CRUD
from Logic.clasa_superioara import clasa_superioara

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
    except:
        print("unknown error")
    return lista


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
            nume=input('Dati numele a carui clasa vreti sa fie trecuta la una superioara: ')
            clasa_superioara(nume,lista)
        elif optiune == '3':
            procentaj=input('Cu ce procentaj se va ieftini rezervarea daca checkin-ul este facut: ')
            procentaj=validare_procent(procentaj)
            ieftinire(procentaj,lista)
        elif optiune == '4':
            max1=get_max1(lista)
            max2=get_max2(lista)
            max3=get_max3(lista)
            print('pretul maxim de la clasa economy este : ',max1)
            print('pretul maxim de la clasa economy plus este : ', max2)
            print('pretul maxim de la clasa business este : ', max3)
        elif optiune == '5':
            show(ordonare_2(lista))
        elif optiune=='6':
            print(sume(lista))
        elif optiune == '7':
            pass
