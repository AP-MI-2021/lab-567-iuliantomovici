def validare_rezervare(ID, nume, clasa, pret, checkin_facut):
    '''
    valideaza datele de intrare si arunca erori in caz de nedeterminare
    :param ID: int
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut:string
    :return: toti parametrii
    '''
    errors = []
    if ID == '':
        errors.append('Id-ul nu poate fi vid')
    try :
        ID=int(ID)
    except ValueError:
        errors.append ('ID ul trebuie sa fie nr intreg')
    if nume == '':
        errors.append('Numele nu poate fi vid')
    if clasa!='business' and clasa!='economy' and clasa!='economy plus':
        errors.append('Clasa nu poate fi vid, nici nu poate avea alte valori decat economy,economy plus sau business')
    try:
        pret = float(pret)
        if pret < 0:
            errors.append('Pretul trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append("Pretul trebuie sa fie un numar real")
    if checkin_facut!='da'and checkin_facut!='nu':
        errors.append('Checkin-ul nu poate fi vid, nici nu poate contine alte valori decat da sau nu')
    if len(errors) != 0:
        raise ValueError(errors)

    return ID, nume, clasa, pret, checkin_facut