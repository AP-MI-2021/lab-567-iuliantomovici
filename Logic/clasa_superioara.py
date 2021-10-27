from Domain.rezervari import get_nume, get_clasa, set_clasa


def clasa_superioara ( nume,lista):
    '''
    Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
    :param nume:string
    :param lista:lista de rezervari
    :return:
    '''
    for rezervare in lista:
        if nume==get_nume(rezervare):
            if get_clasa(rezervare)=='economy':
                set_clasa(rezervare,'economy plus')
            elif get_clasa(rezervare)=='economy plus':
                set_clasa(rezervare,'business')
