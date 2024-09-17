from Film import FilmDVD, FilmVhf, Film
from Formatage.Nettoyage import nettoyage
from Formatage.Tri import tri
from Lieu import verificationLieu


class Bibliotheque:

    def __init__(self, film=[]):
        self.listefilm = film

    def triNom(self):
        listeATri = self.listefilm
        listeNom = sorted(listeATri, key=lambda film: film.nom)
        self.listefilm = listeNom

    def triDateCrois(self):
        listeATri = self.listefilm
        listeTriDateCrois = sorted(listeATri, key=lambda film: film.date)
        self.listefilm = listeTriDateCrois

    def triDateDecrois(self):
        listeATri = self.listefilm
        listeTriDateDecrois = sorted(listeATri, key=lambda film: film.date, reverse=True)
        self.listefilm = listeTriDateDecrois

    def triDVD(self):
        listATri = self.listefilm

        listeDVD = []
        listeVhf = []
        listeAutre = []

        for film in listATri:

            if FilmDVD == type(film):
                listeDVD.append(film)
            elif FilmVhf == type(film):
                listeVhf.append(film)
            else:
                "Format indisponible"
                listeAutre.append(film)

        self.listefilm = listeDVD + listeVhf + listeAutre

    def triVhf(self):
        listATri = self.listefilm

        listeDVD = []
        listeVhf = []
        listeAutre = []

        for film in listATri:

            if FilmDVD == type(film):
                listeDVD.append(film)
            elif FilmVhf == type(film):
                listeVhf.append(film)
            else:
                "Format indisponible"
                listeAutre.append(film)

        self.listefilm = listeVhf + listeDVD + listeAutre


def initBibliotheque(films):
    filmsTrie = []
    for i in range(len(films)):
        filmsTrie.append(tri(films[i][0]))
        filmsTrie[i].append(nettoyage(films[i][1]))

    filmObject = []
    for i in range(len(filmsTrie)):

        if filmsTrie[i][2] == "DVD":
            filmObject.append(FilmDVD(filmsTrie[i][0], filmsTrie[i][1], "bibliotheque"))
        elif filmsTrie[i][2] == "vhf":
            filmObject.append(FilmVhf(filmsTrie[i][0], filmsTrie[i][1], "bibliotheque"))

    return filmObject
