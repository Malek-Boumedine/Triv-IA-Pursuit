import json
import random


class Question :
    def __init__(self):
        pass 

    def random_question():
        with open ("liste_questions.json", "r") as file :
            data = json.load(file)

        a = data["hard_level"]["theme1"].keys()
        b = list(a)
        c = random.choice(b)
        print(c)
#importer question les retourner dans dans variable en fonction du niveau
        

    random_question()

'''
theme, niveau
relié au resultat case

methode pose question : theme selon case , parametre : theme de case 


toutes les questions ont le meme niveau sauf la derniere

importer resultat dé (class joueur) que je stocke dans "result"
si result == jaune : question random theme1
si result == bleu : question random theme2


self.camembert_entier == True
'''