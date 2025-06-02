import json
import random
from case import Case


class Question :
    def __init__(self, enonce : str, reponses : list[str], bonne_reponse : str):
        self.enonce = enonce
        self.reponses = reponses
        self.bonne_reponse = bonne_reponse

    
class GestionQuestions : 
    def __init__(self):
        self.questions_normales = self.importer_questions()[0]
        self.questions_finales = self.importer_questions()[1]
        
    @staticmethod
    def importer_questions() : 
        with open("liste_questions copy.json", "r") as fichier : 
            questions = json.load(fichier)
        questions_normales = questions[0]
        questions_finales = questions[1]
        return questions_normales, questions_finales

    def poser_question(self, case: Case) :
        theme = case.obtenir_theme()
        questions_theme = self.questions_normales[theme]
        cle_question = random.choice(list(questions_theme.keys()))
        enonce = questions_theme[cle_question]["enonce"]
        liste_reponses = questions_theme[cle_question]["reponses"]
        reponse_correcte = questions_theme[cle_question]["reponse_correcte"]
        return enonce, liste_reponses, reponse_correcte

    def poser_question_finale(self) -> Question:
        cle_question = random.choice(list(self.questions_finales.keys()))
        enonce = self.questions_finales[cle_question]["enonce"]
        liste_reponses = self.questions_finales[cle_question]["reponses"]
        reponse_correcte = self.questions_finales[cle_question]["reponse_correcte"]
        return enonce, liste_reponses, reponse_correcte


