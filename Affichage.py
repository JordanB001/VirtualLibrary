from Film import FilmDVD, FilmVhf


def affichageBibliotheque(bibliotheque):

    for film in bibliotheque.listefilm:

        if type(film) == FilmDVD:
            print("Nom :", film.nom, "date :", film.date, "type : DVD")
        elif type(film) == FilmVhf:
            print("Nom :", film.nom, "date :", film.date, "type :vhf")
        else:
            print("Nom :", film.nom, "date :", film.date, "type : ? ")

def affichagePret(maBibliotheque):

    for film in maBibliotheque.listefilm:

        if film.lieu != "bibliotheque":
            print(film.nom, "est chez", film.lieu)






