from copy import deepcopy

from Domain.rezervari import creeaza_rezervare, get_ID, set_nume, set_clasa, set_pret, set_checkin_facut
from Logic.validare import validare_rezervare


def get_by_ID(ID, lista):
    '''
    Gaseste o rezervare dupa un ID dat intr-o lista.
    :param ID: int
    :param lista: lista de rezervari
    :return: rezervarea cu ID-ul dat sau None in caz ca aceasta nu exista
    '''
    for rezervare in lista:
        if get_ID(rezervare) == ID:
            return rezervare
    return None


def adauga_rezervare ( ID, nume, clasa, pret , checkin_facut,lista ) :
    '''
    Adauga o rezervare in lista
    :param ID: int
    :param nume: string
    :param clasa:string
    :param pret: float
    :param checkin_facut:string
    :param lista:lista de rezervari
    :return: lista ce contine rezervarea adaugata cat si pe cele existente
    '''

    ID, nume, clasa, pret , checkin_facut= validare_rezervare( ID, nume, clasa, pret , checkin_facut )
    if ( get_by_ID(ID,lista ) != None ):
        raise ValueError ("ID duplicat")
    rezervare = creeaza_rezervare( ID, nume, clasa, pret , checkin_facut )
    return lista + [rezervare]



def sterge_rezervare(ID, lista):
    '''
    Sterge o rezervare cu ID dat din lista.
    :param ID: int
    :param lista: lista de rezervari
    :return: o lista de rezervari fara elementul cu nr.ID-ului dat
    '''
    return [rezervare for rezervare in lista if get_ID(rezervare) != ID]

def modifica_rezervare(ID, nume, clasa, pret , checkin_facut,lista):
    '''
    Modifica o rezervare cu ID dat din lista
    :param ID: int
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :param lista:lista de rezervari
    :return: lista cu modificarea facuta
    '''
    ID, nume, clasa, pret, checkin_facut, = validare_rezervare(ID, nume, clasa, pret , checkin_facut)
    rez = deepcopy(lista)
    if get_by_ID(ID, lista)==None:
        raise ValueError ('Nu exista ID ul dat')
    for rezervare in rez:
        if get_ID(rezervare) == ID:
            set_nume(rezervare,nume)
            set_clasa(rezervare,clasa)
            set_pret(rezervare,pret)
            set_checkin_facut(rezervare,checkin_facut)
    return rez