from case import Case
from joueur import Joueur
from question2 import GestionQuestions, Question
import json
import random


class Plateau :
    with open("liste_questions copy.json", "r") as fichier:          # importer les thèmes depuis le fichier de questions
        donnees_questions = json.load(fichier)
    THEMES = list(donnees_questions[0].keys())
    rouge, vert, jaune, bleu, magenta, gris, default = "\033[91m", "\033[92m", "\033[93m", '\033[94m', '\033[35m', '\033[90m', '\033[99m'

    COULEURS = {THEMES[0] : rouge, 
                THEMES[1] : vert,
                THEMES[2] : jaune,
                THEMES[3] : bleu,
                THEMES[4] : magenta,
                THEMES[5] : gris}
    
    def __init__(self) :
        self.cases = {}     # dictionnaire avec clé : int et valeur: Case
        self.joueurs = []   # nom des joueurs
        self.gestion_questions = GestionQuestions()
        self.initialiser_plateau()

    def initialiser_plateau(self):

        themes_camemberts = Plateau.THEMES.copy()
        random.shuffle(themes_camemberts)
        
        # création des cases sur le plateau (28 cases)
        for i in range(28):
            i_theme_cam = i // 7    # de 0 à 3 à utiliser pour selectionner des thèmes differents pour chaque camembert
            theme_c = themes_camemberts[i_theme_cam]
            
            if i % 7 == 0 :  # cases camembert tous les 7 cases
                self.cases[i] = Case("camembert", i, theme_c, Plateau.COULEURS[theme_c])
                
            elif i % 7 == 3:  # case relance toutes les 3 cases
                self.cases[i] = Case("relance", i, None, None)
            
            else:  # cases normales
                themes_autres = themes_camemberts.copy()
                if theme_c in themes_autres : 
                    themes_autres.remove(theme_c)
                random.shuffle(themes_autres)
                theme_case = themes_autres[0]
                self.cases[i] = Case("normale", i, theme_case, Plateau.COULEURS[theme_case])
    
    def ajouter_joueur(self, joueur : Joueur):
        self.joueurs.append(joueur)

    def obtenir_case(self, position : list) -> Case:
        return self.cases.get(position)
    
    def obtenir_question_case(self, case: Case) -> Question:
        return GestionQuestions.poser_question(case)

    def obtenir_question_finale(self) -> Question:
        return GestionQuestions.poser_question_finale()
    
    def afficher_plateau(self) : 
        # dimensions
        lignes = 8
        colonnes = 8

        # créer une matrice vide
        matrice = []
        for i in range(lignes) : 
            l0 = []
            for j in range(colonnes) :
                l0.append("  ")
            matrice.append(l0)

        # remplir ligne supérieure
        for i in range(8) :
            matrice[0][i] = self.cases[i] 

        # colonnes
        for i in range(1, 7) :
            matrice[i][0] = self.cases[27-(i-1)]                  # colonne gauche
            matrice[i][colonnes-1] = self.cases[8+(i-1)]          # colonne droite

        # Ligne inférieure
        for i in range(8):
            matrice[7][colonnes-1-i] = self.cases[14+i]      

        # Affichage de la matrice
        for ligne in matrice:
            print(' '.join(f"{str(elem)}" for elem in ligne))





