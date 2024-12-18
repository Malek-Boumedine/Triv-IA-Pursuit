from case import Case
from joueur import Joueur
from question2 import GestionQuestions, Question
import json
import random


class Plateau :
    with open("liste_questions.json", "r") as fichier:          # importer les thèmes depuis le fichier de questions
        donnees_questions = json.load(fichier)
    THEMES = list(donnees_questions[0].keys())

    def __init__(self) :
        self.cases = {}     # dictionnaire avec clé : int et valeur: Case
        self.joueurs = []   # nom des joueurs
        self.initialiser_plateau()

    def initialiser_plateau(self):

        # Création des cases sur le cercle (28 cases)
        for i in range(28):
            position = i % 7    # determiner la position dans le groupe de 7
            liste_themes = Plateau.THEMES.copy()
            index_theme_camembert = 0
            
            if position == 0 :  # cases camembert tous les 7 cases
                theme_camembert = liste_themes[index_theme_camembert]
                self.cases[position] = Case("camembert", position, theme_camembert)
                index_theme_camembert += 1
                            
            elif position == 3:  # case relance toutes les 3 cases
                self.cases[position] = Case("relance", position, None)
            
            else:  # cases normales
                index_case_normale = position - 1 if position < 3 else position - 2
                self.cases[index_case_normale] = Case("normale", index_case_normale, random.choice(liste_themes))

    def ajouter_joueur(self, joueur : Joueur):
        self.joueurs.append(joueur)

    def obtenir_case(self, position : list) -> Case:
        return self.cases.get(tuple(position))
    
    def obtenir_question_case(self, case: Case) -> Question:
        return GestionQuestions.poser_question(case)

    def obtenir_question_finale(self) -> Question:
        return GestionQuestions.poser_question_finale()






