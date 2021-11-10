from Domain.aeroport import get_lista_curenta
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.clasa_superioara import clasa_superioara
from Logic.ieftinire import ieftinire
from Logic.ordonare import ordonare_2
from Logic.pret_maxim import *
from Logic.sume import sume
from Logic.undo_redo import apply_redo, apply_undo
from Logic.validare import validare_procent
from User_Interface.meniu import meniu, meniu_CRUD


def ui_adauga_rezervare(aeroport):
    ID = input('Dati ID-ul rezervarii: ')
    nume = input('Dati numele: ')
    clasa=input('Clasa: ')
    pret= input ('Dati pretul: ')
    checkin_facut = input('Checkin: ')
    try:
        aeroport = adauga_rezervare( ID, nume, clasa, pret, checkin_facut,aeroport)
        print('Rezervarea a fost adaugata cu succes')
        return aeroport
    except ValueError as ve:
        print("au aparut erori",ve)
    except:
        print("unknown error")
    return aeroport


def ui_sterge_rezervare(aeroport):
    ID = int(input('Dati ID-ul rezervarii de sters: '))
    try:
        aeroport = sterge_rezervare(ID,aeroport)
        print('Rezervarea a fost stearsa cu succes')
        return aeroport

    except ValueError as ve:
        print("au aparut erori", ve)
    except:
        print("unknown error")
    return aeroport



def ui_modifica_rezervare(aeroport):
    ID = input('Dati ID-ul rezervarii de modificat: ')
    nume = input('Dati noul nume: ')
    clasa=input('Noua clasa: ')
    pret= input ('Dati noul pret: ')
    checkin_facut = input('Checkin: ')
    try:
        aeroport= modifica_rezervare(ID, nume, clasa, pret , checkin_facut, aeroport)
        print("Rezervarea a fost modificata cu succes!")
        return aeroport
    except ValueError as ve:
        print("au aparut erori",ve)
    except:
        print("unknown error")
    return aeroport

def handle_undo(aeroport):
        apply_undo(aeroport)
        print('Undo facut cu succes')

def handle_redo(aeroport):
        apply_redo(aeroport)
        print('Redo facut cu succes')



def show(aeroport):
    '''
    Afisarea listei de rezervari
    :param aeroport: Lista cu lista de undo, lista curenta si cea de redo
    :return:
    '''
    lista=get_lista_curenta(aeroport)
    for rezervare in lista:
        print(to_string(rezervare))

def consola(aeroport):

    while True:
        meniu()
        optiune = input('Dati optiunea: ')

        if optiune == '1':
            while True:
                meniu_CRUD()
                cmd = input('Dati optiunea: ')
                if cmd=='1':
                    ui_adauga_rezervare(aeroport)
                elif cmd=='2':
                    ui_sterge_rezervare(aeroport)
                elif cmd=='3':
                    ui_modifica_rezervare(aeroport)
                elif cmd == 'a':
                    show (aeroport)
                elif cmd == 'x':
                    break
                else:
                    print('Optiune gresita! Reincercati: ')
        elif optiune=='2':
            nume=input('Dati numele a carui clasa vreti sa fie trecuta la una superioara: ')
            clasa_superioara(nume,aeroport)
        elif optiune == '3':
            procentaj=input('Cu ce procentaj se va ieftini rezervarea daca checkin-ul este facut: ')
            procentaj=validare_procent(procentaj)
            ieftinire(procentaj,aeroport)
        elif optiune == '4':
            max1=get_max1(aeroport)
            max2=get_max2(aeroport)
            max3=get_max3(aeroport)
            print('pretul maxim de la clasa economy este : ',max1)
            print('pretul maxim de la clasa economy plus este : ', max2)
            print('pretul maxim de la clasa business este : ', max3)
        elif optiune == '5':
            print(ordonare_2(aeroport))
        elif optiune=='6':
            print(sume(aeroport))
        elif optiune == '7':
            handle_undo(aeroport)
        elif optiune=='8':
            handle_redo(aeroport)
        else:
            print('optiune invalida! Reincercait: ')
