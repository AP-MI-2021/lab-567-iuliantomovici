from copy import deepcopy

from Domain.rezervari import get_ID, get_pret, to_string
from Logic.CRUD import sterge_rezervare
from Logic.pret_maxim import get_max


def ordonare(lista):
    '''
    Ordoneaza descrescator lista de rezervari in functie de pret
    :param lista: lista de rezervari
    :return: lista ordonata
    '''

    for n in range(len(lista)-1, 0, -1):
        for i in range(n):
            if get_pret(lista[i]) < get_pret(lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista

def ordonare_2(lista):
    '''
    Ordoneaza descrescator lista de rezervari in functie de pret
    :param lista: lista de rezervari
    :return: lista ordonata
    '''
    return sorted(lista, key=lambda rezervare: get_pret(rezervare),reverse=True)



