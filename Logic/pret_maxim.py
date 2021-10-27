from Domain.rezervari import *


def get_max1(lista):
    '''
    Dtermina pretul maxim de la clasa economy
    :param lista: lista de rezervari
    :return: max
    '''
    max=-1
    for rezervare in lista:
        if get_clasa(rezervare)=='economy' and get_pret(rezervare)>max:
            max=get_pret(rezervare)
    return max

def get_max2(lista):
    '''
    Dtermina pretul maxim de la clasa economy plus
    :param lista: lista de rezervari
    :return: max
    '''
    max=-1
    for rezervare in lista:
        if get_clasa(rezervare)=='economy plus' and get_pret(rezervare)>max:
            max=get_pret(rezervare)
    return max

def get_max3(lista):
    '''
    Dtermina pretul maxim de la clasa business
    :param lista: lista de rezervari
    :return: max
    '''
    max=-1
    for rezervare in lista:
        if get_clasa(rezervare)=='business' and get_pret(rezervare)>max:
            max=get_pret(rezervare)
    return max