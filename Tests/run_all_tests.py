from Tests.test_CRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare
from Tests.test_clasa_superioara import test_clasa_superioara
from Tests.test_domain import test_creeaza_rezervare
from Tests.test_ieftinire import test_ieftinire
from Tests.test_ordonare import test_ordonare
from Tests.test_pret_maxim import *


def run_all_tests():
    test_creeaza_rezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_clasa_superioara()
    test_ieftinire()
    test_get_max1()
    test_get_max2()
    test_get_max3()
    test_get_max()
    test_ordonare()