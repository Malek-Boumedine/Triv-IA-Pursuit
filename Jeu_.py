import random

class Jeu:
    
    def __init__(self, type):
        
        self.nom = "TrivIA"
        self.type = type
        self.en_cours = False
        
        print(f"Bienvenue dans le jeu : {self.nom}!")

    def demarrer(self):
        if  not self.en_cours:
            self.en_cours = True

            print(f"Le jeu commence maintenant en {self.type} ! Bonne chance.")
        else:
            print("Le jeu est déjà en cours!")

    def jouer(self):
        if self.type == "solo":
            print("Le jeu est en SOLO!")
        else:
            print("Le jeu est en Multijoueur!")

    def terminer(self):
        if self.en_cours:
            self.en_cours = False
            print(f"Le jeu est terminé!.")
        else:
            print("Le jeu n'est pas en cours.")

    def __str__(self):
        return f"Jeu: {self.nom}"

# Appel de la classe Jeu
if __name__ == "__main__":
    type_jeu = input("Choisir le type de Jeu Solo ou Multi : ")
    mon_jeu = Jeu(type_jeu)
    mon_jeu.demarrer()
    mon_jeu.jouer()
    mon_jeu.terminer()

