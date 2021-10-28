from Logic.CRUD import adauga_rezervare
from Logic.ordonare import ordonare


def test_ordonare():
    lista = []
    lista = adauga_rezervare(2, 'Valicu', 'business', 1000, 'da', lista)
    lista = adauga_rezervare(3, 'John', 'economy', 2000, 'nu', lista)
    lista = adauga_rezervare(5, 'John', 'economy', 2100, 'nu', lista)

    assert ordonare(lista)==[[5, 'John', 'economy', 2100, 'nu'],[3, 'John', 'economy', 2000, 'nu'],[2, 'Valicu', 'business', 1000, 'da']]