from Domain.rezervari import get_clasa
from Logic.CRUD import adauga_rezervare, get_by_ID
from Logic.clasa_superioara import clasa_superioara


def test_clasa_superioara():
    lista = []
    lista = adauga_rezervare('2', 'Valicu', 'business', '1000', 'da', lista)
    lista = adauga_rezervare(3, 'John', 'economy', 2000, 'nu', lista)
    clasa_superioara('John', lista)
    assert get_clasa(get_by_ID(3,lista))=='economy plus'
