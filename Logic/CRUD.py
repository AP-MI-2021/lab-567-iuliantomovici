from Domain.aeroport import adaugare_lista_undo_and_clear_redo, get_lista_curenta
from Domain.rezervari import creeaza_rezervare, get_ID, set_nume, set_clasa, set_pret, set_checkin_facut
from Logic.validare import validare_rezervare


def find_rezervare_index(ID, lista):
    '''
    Gaseste indexul rezervarii dupa ID

    :param lista:lista de rezervari
    :param ID:
    :return:If not found, we return None
    '''
    for i, rezervare in enumerate(lista):
        if str(get_ID(rezervare)) ==str(ID):
            return i
    return None

def get_by_ID(ID, lista):
    '''
    Gaseste o rezervare dupa un ID dat intr-o lista.
    :param ID: int
    :param lista: lista de rezervari
    :return: rezervarea cu ID-ul dat sau None in caz ca aceasta nu exista
    '''
    for rezervare in lista:
        if str(get_ID(rezervare))==str(ID):
            return rezervare
    return None


def adauga_rezervare ( ID, nume, clasa, pret , checkin_facut,aeroport ) :
    '''
    Adauga o rezervare in lista
    :param ID: int
    :param nume: string
    :param clasa:string
    :param pret: float
    :param checkin_facut:string
    :param aeroport:dict
    :return:
    '''
    adaugare_lista_undo_and_clear_redo(aeroport)
    lista=get_lista_curenta(aeroport)
    ID, nume, clasa, pret , checkin_facut= validare_rezervare( ID, nume, clasa, pret , checkin_facut )
    if ( get_by_ID(ID,lista ) != None ):
        raise ValueError ("ID duplicat")
    rezervare = creeaza_rezervare( ID, nume, clasa, pret , checkin_facut )
    lista.append(rezervare)



def sterge_rezervare(ID, aeroport):
    '''
    Sterge o rezervare cu ID dat din lista.
    :param ID: int
    :param aeroport:dict
    :return:
    '''
    adaugare_lista_undo_and_clear_redo(aeroport)
    lista=get_lista_curenta(aeroport)
    index=find_rezervare_index(ID,lista)
    if index!=None:
        lista.pop(index)


def modifica_rezervare(ID, nume, clasa, pret , checkin_facut,aeroport):
    '''
    Modifica o rezervare cu ID dat din lista
    :param ID: int
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :param aeroport:dict
    :return:
    '''
    adaugare_lista_undo_and_clear_redo(aeroport)
    ID, nume, clasa, pret, checkin_facut, = validare_rezervare(ID, nume, clasa, pret , checkin_facut)
    lista=get_lista_curenta(aeroport)

    if get_by_ID(ID, lista)==None:
        raise ValueError ('Nu exista ID ul dat')
    for rezervare in lista:
        if get_ID(rezervare) == ID:
            set_nume(rezervare,nume)
            set_clasa(rezervare,clasa)
            set_pret(rezervare,pret)
            set_checkin_facut(rezervare,checkin_facut)
