from Domain.aeroport import create_aeroport, get_lista_curenta
from Logic.CRUD import adauga_rezervare
from Logic.undo_redo import apply_undo, apply_redo


def test_undo_redo():
    aeroport = create_aeroport()
    adauga_rezervare('4','Valicu','business','1000','da',aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    adauga_rezervare(1,'iulian','economy',122,'da',aeroport)
    assert len(get_lista_curenta(aeroport)) == 3

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 2

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 1

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 0

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 0

    adauga_rezervare('4','Valicu','business','1000','da',aeroport)
    adauga_rezervare('3', 'John', 'economy', '2000', 'nu', aeroport)
    adauga_rezervare(1,'iulian','economy',122,'da',aeroport)
    assert len(get_lista_curenta(aeroport)) == 3

    apply_redo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 3

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 2

    apply_undo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 1

    apply_redo(aeroport)
    assert len(get_lista_curenta(aeroport)) == 2

