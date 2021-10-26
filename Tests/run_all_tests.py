from Tests.test_CRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare
from Tests.test_domain import test_creeaza_rezervare


def run_all_tests():
    test_creeaza_rezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
