from Logic.CRUD import adauga_rezervare
from Logic.pret_maxim import *


def test_get_max1():
    lista = []
    lista = adauga_rezervare('2', 'Valicu', 'business', 1000, 'da', lista)
    lista = adauga_rezervare(3, 'John', 'economy', 2000, 'nu', lista)
    lista = adauga_rezervare(4, 'John', 'economy plus', 2000, 'nu', lista)
    lista = adauga_rezervare(5, 'John', 'economy', 2100, 'nu', lista)
    assert get_max1(lista)==2100
def test_get_max2():
    lista = []
    lista = adauga_rezervare('2', 'Valicu', 'business', 1000, 'da', lista)
    lista = adauga_rezervare(3, 'John', 'economy', 2000, 'nu', lista)
    lista = adauga_rezervare(4, 'John', 'economy plus', 2000, 'nu', lista)
    lista = adauga_rezervare(5, 'John', 'economy', 2100, 'nu', lista)
    assert get_max2(lista)==2000
def test_get_max3():
    lista = []
    lista = adauga_rezervare('2', 'Valicu', 'business', 1000, 'da', lista)
    lista = adauga_rezervare(3, 'John', 'economy', 2000, 'nu', lista)
    lista = adauga_rezervare(4, 'John', 'economy plus', 2000, 'nu', lista)
    lista = adauga_rezervare(5, 'John', 'economy', 2100, 'nu', lista)
    assert get_max3(lista)==1000
