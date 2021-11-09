from Domain.aeroport import create_aeroport, get_lista_curenta
from Logic.CRUD import adauga_rezervare
from Logic.ordonare import ordonare, ordonare_2


def test_ordonare():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)

    assert ordonare_2(aeroport)==[{'ID': 3, 'nume': 'John', 'clasa': 'economy', 'pret': 2000.0, 'checkin_facut': 'nu'}, {'ID': 4, 'nume': 'Valicu', 'clasa': 'business', 'pret': 1000.0, 'checkin_facut': 'da'} ]