from Domain.rezervari import get_pret
from Logic.CRUD import adauga_rezervare, get_by_ID
from Logic.ieftinire import ieftinire


def test_ieftinire():
    lista = []
    lista = adauga_rezervare(1, 'Valicu', 'business', 1000, 'da', lista)
    lista = adauga_rezervare(2, 'John', 'economy', 2000, 'da', lista)
    ieftinire(50,lista)
    rez=get_by_ID(1,lista)
    rec=get_by_ID(2,lista)
    assert get_pret(rez)==500.0
    assert get_pret(rec)==1000.0


