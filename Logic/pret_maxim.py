from Domain.aeroport import get_lista_curenta
from Domain.rezervari import *


def get_max1(aeroport):
    '''
    Dtermina pretul maxim de la clasa economy
    :param aeroport:dict
    :return: max
    '''
    lista=get_lista_curenta(aeroport)
    max=0
    for rezervare in lista:
        if get_clasa(rezervare)=='economy' and get_pret(rezervare)>max:
            max=get_pret(rezervare)
    return max

def get_max2(aeroport):
    '''
    Dtermina pretul maxim de la clasa economy plus
    :param aeroport:dict
    :return: max
    '''
    lista = get_lista_curenta(aeroport)
    max=0
    for rezervare in lista:
        if get_clasa(rezervare)=='economy plus' and get_pret(rezervare)>max:
            max=get_pret(rezervare)
    return max

def get_max3(aeroport):
    '''
    Dtermina pretul maxim de la clasa business
    :param aeroport:dict
    :return: max
    '''
    lista = get_lista_curenta(aeroport)
    max=0
    for rezervare in lista:
        if get_clasa(rezervare)=='business' and get_pret(rezervare)>max:
            max=get_pret(rezervare)
    return max
def get_max(lista):
    '''
    Dtermina pretul maxim
    :param lista: lista de rezervari
    :return: max
    '''
    max = 0
    for rezervare in lista:
        if get_pret(rezervare) > max:
            max = get_pret(rezervare)
    return max