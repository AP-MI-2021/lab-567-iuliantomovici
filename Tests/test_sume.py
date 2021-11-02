from Logic.CRUD import adauga_rezervare
from Logic.sume import sume


def test_sume():
    lista = []
    lista = adauga_rezervare('2', 'Valicu', 'business', 1000, 'da', lista)
    lista = adauga_rezervare(3, 'John', 'economy', 2000, 'nu', lista)
    lista = adauga_rezervare(4, 'John', 'economy plus', 2000, 'nu', lista)
    lista = adauga_rezervare(5, 'John', 'economy', 2100, 'nu', lista)
    assert sume(lista)==[('Valicu',1000),('John',6100)]