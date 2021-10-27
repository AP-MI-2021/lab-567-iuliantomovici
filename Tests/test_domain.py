from Domain.rezervari import *


def test_creeaza_rezervare():
    rezervare= creeaza_rezervare(1,'Popescu Ion','business',1200,'nu')

    assert get_ID(rezervare) == 1
    assert get_nume(rezervare) == 'Popescu Ion'
    assert get_clasa(rezervare) == 'business'
    assert get_pret(rezervare) == 1200
    assert get_checkin_facut(rezervare) =='nu'
    set_nume(rezervare,'ionut')
    assert get_nume(rezervare)=='ionut'
    set_pret(rezervare,123)
    assert get_pret(rezervare)==123
    set_clasa(rezervare,'economy')
    set_checkin_facut(rezervare,'da')
    assert get_clasa(rezervare)=='economy'
    assert get_checkin_facut(rezervare)=='da'