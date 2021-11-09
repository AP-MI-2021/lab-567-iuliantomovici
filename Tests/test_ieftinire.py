from Domain.aeroport import create_aeroport, get_lista_curenta
from Domain.rezervari import get_pret
from Logic.CRUD import adauga_rezervare, get_by_ID
from Logic.ieftinire import ieftinire


def test_ieftinire():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    ieftinire(50,aeroport)
    lista=get_lista_curenta(aeroport)
    rez=get_by_ID(4,lista)
    rec=get_by_ID(3,lista)
    assert get_pret(rez)==500.0
    assert get_pret(rec)==2000.0


