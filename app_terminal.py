from joueur import Joueur
from plateau import Plateau
import random
import os


print("\n", "-"*50, "TRIV-IA Pursuit", "-"*50, "\n")
print("#"*5, "CONFIGURATION DU JEU", "#"*5, "\n")

plateau1 = Plateau()
themes_camembert = [case.theme for case in plateau1.cases.values() if case.coordonnees % 7 == 0]         # liste des themes camembert du plateau, a utiliser avec afficher_camemberts()
print(themes_camembert)

while True :
    try :   
        nombre_joueurs = int(input("Saisissez le nombre de joueurs : "))
        if nombre_joueurs < 0 : 
            print("Veuillez saisir un nombre positif ! \n")
            continue
        elif nombre_joueurs == 0 :
            print("Veuillez saisir un nombre supérieur à zéro ! \n")
            continue
        break
    except ValueError : 
        print("Veuillez saisir un nombre entier\n")

for i in range(nombre_joueurs) :                            # création du plateau avec les différents joueurs
    nom = input(f"Saisissez le nom du joueur {i+1} : ")     # saisir le nom de chaque joueur
    position = random.choice([3, 10, 17, 24])               # position de départ depuis une case relance
    plateau1.ajouter_joueur(Joueur(nom, position))          # ajout des différents joueurs au plateau
print(f"\nListe des joueurs : {[j.nom for j in plateau1.joueurs]}")
input("\n\nENTREE pour commencer à jouer !")

os.system('clear')

joueurs = plateau1.joueurs                                  # stocker les joueurs 

jeu_fini = False
while not jeu_fini : 
    for j in joueurs : 
        marche = True
        while marche : 
            if j.camembert_entier == True :         # si le joueur a récolté tous les camemberts
                print("-"*50, "TRIV-IA Pursuit", "-"*50)
                print("\nVous avez récolté tous les camemberts ! \nQuestion finale : \n")
                q_finale = plateau1.gestion_questions.poser_question_finale()
                enonce = q_finale[0]
                reponses = q_finale[1]
                reponse_correcte = q_finale[2]
                print(f"\nQuestion : {enonce} \n")
                for i,choix in enumerate(reponses) :                # choix à l'indice 1
                    print(f"{i+1} - {choix}")                       # afficher tous les choix
                
                while True:
                    try:
                        reponse_saisie = int(input("\nSaisissez le numéro de votre réponse : ")) 
                        if reponse_saisie not in [1,2,3,4] :
                            print("Vous devez saisir un nombre entre 1 et 4") 
                            continue
                        break  # Sort de la boucle si la réponse est valide
                    except ValueError:
                        print("Vous devez saisir un nombre entier")                    
                    
                if reponses[reponse_saisie-1] == reponse_correcte :
                    print("👏 👏 🎊 🎊  BRAVO ! VOUS AVEZ GAGNE 🎊 🎊 🎊")
                    print("MERCI d'avoir joué. Au revoir\n")
                    print("-"*50, " FIN DU JEU ", "-"*50)
                    jeu_fini = True
                    break
                else : 
                    print("😭 😭 😭 Mauvaise réponse ! Au tour du joueur suivant")
                    break
            else :
                print("-"*50, "TRIV-IA Pursuit", "-"*50)
                print(f"\nTour de {j.nom} !\n\n")
                # print("camemberts joueur : ", j.camemberts)
                j.afficher_camemberts(themes_camembert)
                print()
                position_initiale = j.position
                print(f"Position actuelle de {j.nom} : {position_initiale}")
                print(j.se_deplacer(), "\n")
                position_apres_deplacement = j.position
                plateau1.cases[position_apres_deplacement].joueur_dessus = True
                print(f"Nouvelle position de {j.nom} : {position_apres_deplacement}")
                # debogage
                print("case : ",plateau1.cases[position_apres_deplacement].obtenir_position())
                
                plateau1.afficher_plateau()
                case_joueur = plateau1.cases[position_apres_deplacement]                # chercher la case sur laquelle le joueur se trouve
                theme_case = case_joueur.obtenir_theme()
                
                if not case_joueur.est_case_relance() : 
                    question = plateau1.gestion_questions.poser_question(case_joueur)
                    enonce = question[0]            # enonce de la question
                    reponses = question[1]          # liste des reponses
                    reponse_correcte = question[2]  # reponse correcte 
                    print(f"Vous êtes tombé sur une case de thème '{theme_case}'")
                    if case_joueur.est_case_camembert() and not j.camemberts[theme_case] : 
                        print("⚠️   Tentez de gagner le camembert de ce thème   ⚠️")
                        
                    print(f"\nQuestion : {enonce} \n")                    # enoncé à l'indice 0
                    for i,choix in enumerate(reponses) :                # choix à l'indice 1
                        print(f"{i+1} - {choix}")                       # afficher tous les choix
                        
                    while True:
                        try:
                            reponse_saisie = int(input("\nSaisissez le numéro de votre réponse : "))
                            if reponse_saisie not in [1,2,3,4]:
                                print("Vous devez saisir un nombre entre 1 et 4")
                                continue
                            break  # Sort de la boucle si la réponse est valide
                        except ValueError:
                            print("Vous devez saisir un nombre entier")                    

                    if reponses[reponse_saisie-1] == reponse_correcte : 
                        if case_joueur.est_case_camembert() :           # si c'est une case camembert
                            if not j.camemberts[theme_case] :           # si le camembert du thème de la case n'est pas deja obtenu
                                j.ajouter_camembert(theme_case)         # ajout du camembert
                                print(f"👏 👏 Bravo vous venez de gagner le camembert du thème '{theme_case}'. Vous continuez à jouer ! ")
                                # vérifier si le joueur a tous les camemberts pour lancer la question finale
                                nombre_themes_obtenus = len([x for x in j.camemberts.values() if x == True])
                                if nombre_themes_obtenus == 4 :
                                    j.camembert_entier = True
                        else : 
                            print("👏 Bonne réponse, vous continuez ! \n")

                    else : 
                        print(f"Mauvaise réponse ! la réponse correcte était {reponse_correcte}")
                        marche = False
                        # break

                else  : 
                    print("🎲 Vous êtes tombé sur une case relancer, vous allez rejouer ! 🎲 \n")
                
                print("\n","-"*50)
                input("ENTREE")
                os.system('clear')
                plateau1.cases[position_apres_deplacement].joueur_dessus = False
    
    



