from Domain.rezervari import get_checkin_facut, get_pret, set_pret


def ieftinire(procentaj,lista):
    '''
    Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.
    :param procentaj: float
    :param lista: lista de rezervari
    :return:
    '''
    for rezervare in lista:
        if get_checkin_facut(rezervare)=='da':
            pret_redus=float(get_pret(rezervare))-((float(get_pret(rezervare))*procentaj)//100)
            set_pret(rezervare,pret_redus)