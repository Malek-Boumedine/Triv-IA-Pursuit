import random
from case import Case
import json

class Joueur:
    with open("liste_questions copy.json", "r") as fichier:          # importer les thèmes depuis le fichier de questions
        donnees_questions = json.load(fichier)
    THEMES = list(donnees_questions[0].keys())

    def __init__(self, nom: str, position : int):
        self.nom = nom[0].upper()+nom[1:].lower()
        self.position = position  # [de 0 à 28]
        self.camembert_entier = False
        self.camemberts = {
            Joueur.THEMES[0] : False,
            Joueur.THEMES[1] : False,
            Joueur.THEMES[2] : False,
            Joueur.THEMES[3] : False,
            Joueur.THEMES[4] : False,
            Joueur.THEMES[5] : False}

    def lancer_de(self) -> int :
        return 1
        # return random.randint(1, 6)

    def se_deplacer(self) -> str :
        input("Appuyez sur Entree pour lancer le dé ! 🎲 ")
        resultat_de = self.lancer_de()
        self.position = (self.position + resultat_de) % 28
        return(f"\t🎲 {self.nom} a obtenu un {resultat_de} ! 🎲")

    def tenter_gagner_camembert(self, case : Case, theme : str) :  
        if case.est_case_camembert(): 
            self.ajouter_camembert(theme)

    def ajouter_camembert(self, theme:str) : 
        self.camemberts[theme] = True
        if all(self.camemberts.values()) :
            self.camembert_entier = True 
            
    def afficher_camemberts(self, themes_plateau : list) : 
        print(f"Camemberts de {self.nom} : ", end= "   ")
        for i,j in self.camemberts.items() : 
            if i in themes_plateau :
                print(f"{i} : ✅" if j else f"{i} : ❌", end=" | ")
        print()
                        
            

