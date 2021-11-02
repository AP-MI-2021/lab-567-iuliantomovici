from Logic.CRUD import adauga_rezervare
from Logic.ordonare import ordonare, ordonare_2


def test_ordonare():
    lista = []
    lista = adauga_rezervare(2, 'Valicu', 'business', 1000, 'da', lista)
    lista = adauga_rezervare(3, 'John', 'economy', 2000, 'nu', lista)
    lista = adauga_rezervare(5, 'John', 'economy', 2100, 'nu', lista)

    assert ordonare_2(lista)==[{'ID': 5, 'nume': 'John', 'clasa': 'economy', 'pret': 2100.0, 'checkin_facut': 'nu'}, {'ID': 3, 'nume': 'John', 'clasa': 'economy', 'pret': 2000.0, 'checkin_facut': 'nu'}, {'ID': 2, 'nume': 'Valicu', 'clasa': 'business', 'pret': 1000.0, 'checkin_facut': 'da'}]