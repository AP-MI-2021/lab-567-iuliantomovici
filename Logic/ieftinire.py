from Domain.aeroport import adaugare_lista_undo_and_clear_redo, get_lista_curenta
from Domain.rezervari import get_checkin_facut, get_pret, set_pret


def ieftinire(procentaj,aeroport):
    '''
    Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.
    :param procentaj: float
    :param aeroport:dict
    :return:
    '''
    adaugare_lista_undo_and_clear_redo(aeroport)
    lista = get_lista_curenta(aeroport)
    for rezervare in lista:
        if get_checkin_facut(rezervare)=='da':
            pret_redus=float(get_pret(rezervare))-((float(get_pret(rezervare))*procentaj)//100)
            set_pret(rezervare,pret_redus)