from Domain.aeroport import get_lista_curenta, create_aeroport
from Logic.CRUD import adauga_rezervare
from Logic.sume import sume


def test_sume():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    adauga_rezervare('5', 'John', 'economy', '4100', 'nu', aeroport)

    lista=get_lista_curenta(aeroport)
    assert sume(lista)==[('Valicu',1000),('John',6100)]