

from Domain.aeroport import adaugare_lista_undo_and_clear_redo, get_lista_curenta
from Domain.rezervari import *

#varianta 1 de ordonare
"""def ordonare(lista):
    '''
    Ordoneaza descrescator lista de rezervari in functie de pret
    :param lista: lista de rezervari
    :return: lista ordonata
    '''

    for n in range(len(lista)-1, 0, -1):
        for i in range(n):
            if get_pret(lista[i]) < get_pret(lista[i + 1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista"""

def ordonare_2(aeroport):
    '''
    Ordoneaza descrescator lista de rezervari in functie de pret
    :param aeroport:dict
    :return: lista ordonata
    '''
    lista = get_lista_curenta(aeroport)
    return sorted(lista, key=lambda rezervare: get_pret(rezervare),reverse=True)



