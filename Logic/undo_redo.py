from Domain.aeroport import *


def apply_undo(aeroport):
    '''
    aplica undo listei
    :param aeroport: dict
    :return:
    '''
    lista_undo = get_lista_undo(aeroport)
    if len(lista_undo) > 1:
        adaugare_lista_redo(aeroport)
        prior_lista_curenta = lista_undo.pop()
        set_lista_curenta(aeroport, prior_lista_curenta)
    else:
        set_lista_curenta(aeroport, [])



def apply_redo(aeroport):
    '''
    aplica redo
    :param aeroport: dict
    :return:
    '''
    lista_redo = get_lista_redo(aeroport)
    if len(lista_redo) > 0:
        adaugare_lista_undo(aeroport)
        new_current_list = lista_redo.pop()
        set_lista_curenta(aeroport, new_current_list)