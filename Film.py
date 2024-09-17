class Film:

    def __init__(self, nom, date, lieu):
        self.nom = nom
        self.date = date
        self.lieu = lieu

class FilmVhf(Film):
    pass


class FilmDVD(Film):
    pass
