from Domain.rezervari import creeaza_rezervare,get_ID,get_nume,get_pret,get_clasa,get_checkin_facut
def test_creeaza_rezervare():
    rezervare= creeaza_rezervare(1,'Popescu Ion','business',1200,'nu')

    assert get_ID(rezervare) == 1
    assert get_nume(rezervare) == 'Popescu Ion'
    assert get_clasa(rezervare) == 'business'
    assert get_pret(rezervare) == 1200
    assert get_checkin_facut(rezervare) =='nu'

