from copy import deepcopy

from Domain.rezervari import get_ID, get_pret
from Logic.CRUD import sterge_rezervare
from Logic.pret_maxim import get_max


def ordonare(lista):
    '''
    Ordoneaza descrescator lista de rezervari in functie de pret
    :param lista: lista de rezervari
    :return: rez :lista ordonata
    '''
    rez=[]
    aux=deepcopy(lista)
    while len(aux)>0:
        for rezervare in aux:
            if get_max(aux)==get_pret(rezervare):
                rez.append(rezervare)
                id=get_ID(rezervare)
                sterge_rezervare(id,aux)
                break
    return rez




