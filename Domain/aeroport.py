from copy import deepcopy


def create_aeroport():
    '''
    Creeaza un dictionar ce contine lista curenta si listele de undo si redo
    :return: dict
    '''

    return {
        'lista_curenta': [],
        'lista_undo': [[]],
        'lista_redo': []
    }
def get_lista_curenta(aeroport):
    '''
    Da lista curenta
    :param aeroport:dict
    :return: aeroport['lista_curenta']
    '''
    return aeroport['lista_curenta']

def get_lista_undo(aeroport):
    '''
    Da lista undo
    :param aeroport: dict
    :return: aeroport['lista_undo']
    '''
    return aeroport['lista_undo']

def get_lista_redo(aeroport):
    '''
    Da lista redo
    :param aeroport: dict
    :return:aeroport['lista_redo']
    '''
    return aeroport['lista_redo']

def set_lista_curenta(aeroport, new_current_list):
    '''
    Seteaza lista curenta
    :param aeroport: dict
    :param new_current_list: lista
    :return: aeroport['lista_curenta'] = new_current_list
    '''
    aeroport['lista_curenta'] = new_current_list

def adaugare_lista_undo(aeroport):
    '''
    copiaza lista curenta in lista undo
    :param aeroport: dict
    :return:
    '''
    lista_curenta = get_lista_curenta(aeroport)
    get_lista_undo(aeroport).append(deepcopy(lista_curenta))

def clear_redo(aeroport):
    '''
    Curata lista redo
    :param aeroport: dict
    :return:
    '''
    get_lista_redo(aeroport).clear()
def adaugare_lista_redo(aeroport):
    '''
    copiaza in lista redo lista curenta
    :param aeroport: dict
    :return:
    '''
    lista_curenta = get_lista_curenta(aeroport)
    get_lista_redo(aeroport).append(deepcopy(lista_curenta))

# functia se va apela pentru operatiile care modifica listaCurenta
def adaugare_lista_undo_and_clear_redo(aeroport):
    '''
    Apeleaza functia care adauga in undo si curata redo
    :param aeroport:
    :return:
    '''
    adaugare_lista_undo(aeroport)
    clear_redo(aeroport)



