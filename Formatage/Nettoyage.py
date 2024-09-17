def nettoyage(chaine):
    """
    Corrige les majuscules et minuscules des chaines de caractere DVD ou vhf
    :param chaine:
    :return:
    """

    if chaine.lower() == "vhf":
        chaineNettoye = chaine.lower()
    elif chaine.upper() == "DVD":
        chaineNettoye = chaine.upper()
    else:
        raise Exception("format invalide")

    return chaineNettoye
