from Domain.aeroport import adaugare_lista_undo_and_clear_redo, get_lista_curenta
from Domain.rezervari import get_nume, get_clasa, set_clasa


def clasa_superioara ( nume,aeroport):
    '''
    Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
    :param nume:string
    :param aeroport:dict
    :return:
    '''
    adaugare_lista_undo_and_clear_redo(aeroport)
    lista = get_lista_curenta(aeroport)
    for rezervare in lista:
        if nume==get_nume(rezervare):
            if get_clasa(rezervare)=='economy':
                set_clasa(rezervare,'economy plus')
            elif get_clasa(rezervare)=='economy plus':
                set_clasa(rezervare,'business')
