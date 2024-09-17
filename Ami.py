class Ami:

    def __init__(self, nom, filmpossede=""):
        self.nom = nom
        self.film = filmpossede



def initAmi(listeAmisRaw):

    listeAmi = []

    for ami in listeAmisRaw:
        try:
            listeAmi.append(Ami(ami[0], ami[1]))
        except IndexError:
            listeAmi.append(Ami(ami[0]))

    return listeAmi



