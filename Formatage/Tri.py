def tri(chaine):
    """
    Prends une chaine de caractere à trier avec la date en () en renvoi une liste avec le nom et la date séparé
    :param chaine:
    :return:
    """
    nomFilm = chaine.split("(")[0]

    chaine1 = chaine.split("(")[1]
    date = chaine1.split(")")[0]
    chaineTrie = [nomFilm.strip(), date]

    return chaineTrie