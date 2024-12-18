import random
from case import Case


class Joueur:
    def __init__(self, nom: str, position : int):
        self.nom = nom
        self.position = position  # [de 0 à 28]
        self.camembert_entier = False
        self.camemberts = {
            "T1": False,
            "T2": False,
            "T3": False,
            "T4": False
        }

    def lancer_de(self) -> int :
        return random.randint(1, 6)

    def se_deplacer(self) -> str :
        input("Appuyez sur Entree pour lancer le dé ! ")
        resultat_de = self.lancer_de()
        self.position += resultat_de
        return (f"{self.nom} a obtenu un {resultat_de} au lancé de dé ! ")

    def tenter_gagner_camembert(self, case : Case, theme : str) :  
        if case.est_case_camembert(): 
            self.ajouter_camembert(theme)

    def ajouter_camembert(self, theme:str) : 
        self.camemberts[theme] = True
        if all(self.camemberts.values()) :
            self.camembert_entier = True 
            
    def rejouer(self, case : Case) : 
        if case.est_case_relance : 
            self.se_deplacer
            
            

