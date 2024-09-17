def verificationLieu(maBibliotheque, listeAmi):

    for ami in listeAmi:
        for film in maBibliotheque.listefilm:
            if ami.film == film.nom:
                film.lieu = ami.nom




