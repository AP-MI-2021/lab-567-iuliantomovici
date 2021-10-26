from Domain.rezervari import get_ID, get_nume, get_pret, get_clasa, get_checkin_facut
from Logic.CRUD import adauga_rezervare, get_by_ID, sterge_rezervare, modifica_rezervare


def test_adauga_rezervare():
    lista=[]
    lista= adauga_rezervare('2','Valicu','business','1000','da',lista)
    assert len(lista) == 1
    assert get_ID(get_by_ID(2, lista)) == 2
    assert get_nume(get_by_ID(2, lista)) =='Valicu'
    assert get_clasa(get_by_ID(2, lista)) == 'business'
    assert get_pret(get_by_ID(2, lista)) == 1000


def test_sterge_rezervare():
    lista = []
    lista = adauga_rezervare(2,'Valicu','business',1000,'da',lista)
    lista = adauga_rezervare(3,'John','economy',2000,'nu', lista)

    lista = sterge_rezervare(2, lista)

    assert len(lista) == 1
    assert get_by_ID(2, lista) is None
    assert get_by_ID(3, lista) is not None

    lista = sterge_rezervare(8, lista)

    assert len(lista) == 1
    assert get_by_ID(3, lista) is not None

def test_modifica_rezervare():
    lista = []
    lista = adauga_rezervare(2, 'Valicu', 'business', 1000, 'da', lista)
    lista = adauga_rezervare(3, 'John', 'economy', 2000, 'nu', lista)

    lista= modifica_rezervare(3, 'John', 'economy plus', 3000, 'da', lista)
    rezervare_modificata=get_by_ID(3, lista)
    assert get_ID(rezervare_modificata) == 3
    assert get_nume(rezervare_modificata) == 'John'
    assert get_pret(rezervare_modificata) == 3000
    assert get_checkin_facut(rezervare_modificata) == 'da'

