"""
Voici un programme de gestion de Bibibliotheque de film
Il s'agit d'un exercice d'Openclassroom : https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7196906-decomposez-un-probleme-de-programmation-orientee-objet

Creator : BIGRE Jordan
"""
from Ami import initAmi
from Bibliotheque import Bibliotheque, initBibliotheque
from Formatage.Tri import tri
from Formatage.Nettoyage import nettoyage
from Film import Film, FilmVhf, FilmDVD
from Affichage import affichageBibliotheque, affichagePret
from Lieu import verificationLieu
from hasard import recupererFilmHasard

films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD"),
    ("L'Empire contre-attaque (1980)", "vhf"),
    ("Retour vers le futur (1985)", "vhf"),
    ("La Guerre des Étoiles (1977)", "vhf"),
    ("L'Armée des 12 singes (1995)", "dVd"),
    ("Terminator 2 : Le Jugement dernier (1991)", "DVD"),
]

friends = [
    ("Paul", "Blade Runner"),
    ("Lucie",),
    ("Zoé", "Terminator 2 : Le Jugement dernier"),
]



#Init des films et des amis
amis = initAmi(friends)
filmObject = initBibliotheque(films)

#Init de la bibliotheque
bibliothequeVirtuelle = Bibliotheque(filmObject)
verificationLieu(bibliothequeVirtuelle, amis)

#-------------- COMMANDE DIVERSE -----------------

bibliothequeVirtuelle.triNom()
affichageBibliotheque(bibliothequeVirtuelle)
print("\n")

print(recupererFilmHasard(bibliothequeVirtuelle).nom)

