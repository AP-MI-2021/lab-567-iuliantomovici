from Domain.aeroport import get_lista_curenta
from Domain.rezervari import get_nume, get_pret


def sume(aeroport):
    '''
    Calculeaza suma prturilor rezervarilor pentru fiecare nume
    :param lista: lista de rezervari
    :return: sumele:lista de tuple ce contin numele si suma preturilor
    '''
    numele=[]
    sumele=[]
    lista = get_lista_curenta(aeroport)
    for rezervare in lista:
        if get_nume(rezervare) not in numele:
            numele.append(get_nume(rezervare))
    for i in range (0,len(numele)):
        suma=0
        for rezervare in lista:
            if get_nume(rezervare)==numele[i]:
                suma=suma+get_pret(rezervare)
        sumele.append((numele[i],suma))
    return sumele




