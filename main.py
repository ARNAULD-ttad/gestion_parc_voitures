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
v1 = Voiture("Toyota", "Corolla", "AA111")
v2 = Voiture("BMW", "X5", "BB222")
v3 = Voiture("Audi", "A4", "CC333")
v4 = Voiture("Mercedes", "C300", "DD444")
parc.entrerVoiture(v1)
parc.entrerVoiture(v2)
parc.entrerVoiture(v3)
parc.entrerVoiture(v4)