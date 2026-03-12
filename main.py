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