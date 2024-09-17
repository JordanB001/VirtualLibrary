from random import randint


def recupererFilmHasard(maBibliotheque):

    nbrDeFilm = len(maBibliotheque.listefilm)
    nbrRandom = randint(0, nbrDeFilm - 1)

    return maBibliotheque.listefilm[nbrRandom]



