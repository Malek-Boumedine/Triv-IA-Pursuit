import json
import random


class Question :
    def __init__(self, theme, niveau):
        self.theme = theme
        self.niveau = niveau

    # def recuperer_questions():
    #     with open ("liste_questions.json", "r") as file :
    #         data = json.load(file)

    #     for level_data in data:
    #         if level_data["level"] == "easy_level":
    #             # print("Les questions easy_level th1 :")
    #             for theme, questions in level_data.items():
    #                 if theme == "theme1":  
    #                     question_simple_th1 = [] 
    #                     for question in questions.keys():
    #                         a = (f"  {question} ")
    #                         question_simple_th1.append(a)

        



    #     for level_data in data:
    #         if level_data["level"] == "easy_level":
    #             # print("Les questions easy_level th2 :")
    #             for theme, questions in level_data.items():
    #                 if theme == "theme2":  
    #                     question_simple_th2 = [] 
    #                     for question in questions.keys():
    #                         b = (f"  {question} ")
    #                         question_simple_th2.append(b)
                        

        
        
        # print("Les questions easy_level th1 :" f"{question_simple_th1}")
        # print("Les questions easy_level th2 :" f"{question_simple_th2}")
        



                            





                # b = random.choice(liste_question_simple)
                # print(b)


        

    # recuperer_questions()

'''
relié au resultat case

methode pose question : theme selon case , parametre : theme de case 


toutes les questions ont le meme niveau sauf la derniere

importer resultat dé (class joueur) que je stocke dans "result"
si result == jaune : question random theme1
si result == bleu : question random theme2


self.camembert_entier == True
'''


# with open ("liste_questions2.json", "r") as file2 :
#     data2 = json.load(file2)

# question_facile = data2[0]
# print(question_facile)


with open ("liste_questions.json", "r") as file :
    data = json.load(file)


# theme1 = data[0]["theme1"]
# first_question = list(theme1.keys())[1]

first_question = list(data[0]["theme1"].keys())[0]
print(first_question)




