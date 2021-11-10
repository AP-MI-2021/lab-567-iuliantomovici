from Domain.aeroport import create_aeroport, get_lista_curenta
from Logic.CRUD import adauga_rezervare
from Logic.pret_maxim import *


def test_get_max1():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    lista=get_lista_curenta(aeroport)
    assert get_max1(aeroport)==2000
def test_get_max2():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    lista=get_lista_curenta(aeroport)
    assert get_max2(aeroport)==0
def test_get_max3():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    lista=get_lista_curenta(aeroport)
    assert get_max3(aeroport)==1000
def test_get_max():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    lista=get_lista_curenta(aeroport)
    assert get_max(lista) == 2000

