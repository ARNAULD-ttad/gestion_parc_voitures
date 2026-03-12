class Voiture:

    def __init__(self, marque, modele, immatriculation):
        self.marque = marque
        self.modele = modele
        self.immatriculation = immatriculation

    def afficher_info(self):
        print("Marque :", self.marque)
        print("Modele :", self.modele)
        print("Immatriculation :", self.immatriculation)
class Parc:

    def __init__(self, capacite):
        self.capacite = capacite
        self.voitures = []

    def entrerVoiture(self, voiture):

        if voiture in self.voitures:
            print("La voiture est déjà dans le parc")
            return

        if len(self.voitures) >= self.capacite:
            print("Le parc est plein")
            return

        self.voitures.append(voiture)
        print("Voiture ajoutée au parc")

    def sortirVoiture(self, voiture):

        if voiture not in self.voitures:
            print("La voiture n'est pas dans le parc")
            return

        self.voitures.remove(voiture)
        print("Voiture retirée du parc")

        print("Places libres :", self.calculerNbrPlacesLibres())

    def calculerNbrPlacesLibres(self):

        return self.capacite - len(self.voitures)
parc = Parc(3)