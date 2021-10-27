def creeaza_rezervare(ID, nume, clasa, pret , checkin_facut):
    '''
    Creeaza o lista cu rezervarile
    :param ID: int
    :param nume: string
    :param clasa:string: 'economy','economy plus',or 'business'
    :param pret: float
    :param checkin_facut: string: 'da' sau 'nu'
    :return: un dictionar ce contine o rezervre
    '''
    lista=[]
    return lista + [ID,nume,clasa,pret,checkin_facut]

def get_ID(rezervare):
    '''
    Da ID-ul rezervarii
    :param rezervare: dict
    :return:ID-ul rezervarii
    '''
    for i in range(0, len(rezervare)-1):
        ID=rezervare[0]
    return  ID

def get_nume(rezervare):
    '''
    Da numele pe care e facuta rezervarea
    :param rezervare: dict
    :return: numele rezervarii
    '''
    for i in range(0, len(rezervare)-1):
        nume=rezervare[1]
    return  nume


def get_clasa(rezervare):
    '''
    Da clasa la care este facuta rezervarea
    :param rezervare: dict
    :return: clasa la care este facuta rezervarea
    '''
    for i in range(0, len(rezervare) - 1):
        clasa = rezervare[2]
    return clasa


def get_pret(rezervare):
    '''
    Da pretul zborului
    :param rezervare: dict
    :return: pretul zborului
    '''
    for i in range(0, len(rezervare) - 1):
        pret = rezervare[3]
    return pret


def get_checkin_facut(rezervare):
    '''
    Da statusul checkin-ului
    :param rezervare: dict
    :return: statusul checkin-ului
    '''
    for i in range(0, len(rezervare) - 1):
        checkin_facut=rezervare[4]
    return checkin_facut




def set_nume(rezervare,nume):
    '''
    Seterea numelui rezervarii
    :param rezervare: dict
    :param nume: string
    :return:
    '''
    for i in range(0, len(rezervare) - 1):
        rezervare[1]=nume

def set_clasa(rezervare,clasa):
    '''
    Setarea clasei rezervarii
    :param rezervare: dict
    :param clasa: string
    :return:
    '''
    for i in range(0, len(rezervare) - 1):
        rezervare[2]=clasa


def set_pret(rezervare,pret):
    '''
    Seterea pretului rezervarii
    :param rezervare: dict
    :param pret: float
    :return:
    '''
    for i in range(0, len(rezervare) - 1):
        rezervare[3]=pret

def set_checkin_facut(rezervare,checkin_facut):
    '''
    Seterea statusului checkin ului rezervarii
    :param rezervare: dict
    :param :cehckin_facut: string
    :return:
    '''
    for i in range(0, len(rezervare) - 1):
        rezervare[4]=checkin_facut


def to_string(rezervare):
    return 'ID: {}, nume: {}, clasa: {}, pret: {}, checkin_facut: {} '.format(
        get_ID(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin_facut(rezervare)   )


