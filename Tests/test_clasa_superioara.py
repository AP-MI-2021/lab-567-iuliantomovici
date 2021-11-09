from Domain.aeroport import create_aeroport, get_lista_curenta
from Domain.rezervari import get_clasa
from Logic.CRUD import adauga_rezervare, get_by_ID
from Logic.clasa_superioara import clasa_superioara


def test_clasa_superioara():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    clasa_superioara('John', aeroport)
    lista= get_lista_curenta(aeroport)
    assert get_clasa(get_by_ID(3,lista))=='economy plus'
