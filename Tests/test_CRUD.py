from Domain.aeroport import *
from Domain.rezervari import get_ID, get_nume, get_pret, get_clasa, get_checkin_facut, creeaza_rezervare
from Logic.CRUD import adauga_rezervare, get_by_ID, sterge_rezervare, modifica_rezervare, find_rezervare_index


def test_adauga_rezervare():
    aeroport = create_aeroport()
    adauga_rezervare('4','Valicu','business','1000','da',aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    assert len(get_lista_curenta(aeroport))==2
    assert get_nume(get_by_ID(4, get_lista_curenta(aeroport))) =='Valicu'
    assert get_clasa(get_by_ID('3', get_lista_curenta(aeroport))) == 'economy'
    assert get_pret(get_by_ID('4', get_lista_curenta(aeroport))) == 1000
    adauga_rezervare('5','eff','economy','1','da',aeroport)
    assert len(get_lista_curenta(aeroport)) == 3


def test_sterge_rezervare():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)

    assert len(get_lista_curenta(aeroport)) == 2
    assert get_by_ID(2, get_lista_curenta(aeroport)) is None
    assert get_by_ID(3, get_lista_curenta(aeroport)) is not None
    lista=get_lista_curenta(aeroport)
    sterge_rezervare('4', aeroport)

    assert len(lista) == 1
    assert get_by_ID(4, get_lista_curenta(aeroport)) is None

def test_modifica_rezervare():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    modifica_rezervare('3', 'John', 'economy plus', '3000', 'da', aeroport)
    lista=get_lista_curenta(aeroport)
    rezervare_modificata=get_by_ID('3', lista)
    assert get_ID(rezervare_modificata) == 3
    assert get_nume(rezervare_modificata) == 'John'
    assert get_pret(rezervare_modificata) == 3000.0
    assert get_checkin_facut(rezervare_modificata) =='da'

def test_get_by_ID():
    aeroport = create_aeroport()
    adauga_rezervare('4', 'Valicu', 'business', '1000', 'da', aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    adauga_rezervare('5', 'John', 'economy', '4100', 'nu', aeroport)
    lista=get_lista_curenta(aeroport)
    assert get_nume(get_by_ID(4,lista))=='Valicu'
    assert find_rezervare_index(4,lista)==0


