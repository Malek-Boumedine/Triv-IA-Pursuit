from joueur import Joueur
from plateau import Plateau
import random
import os


print("-"*100)
print("TRIV-IA Pursuit")
plateau1 = Plateau()

nombre_joueurs = int(input("Saisissez le nombre de joueurs : "))

for i in range(nombre_joueurs) :                            # création du plateau avec les différents joueurs
    nom = input(f"Saisissez le nom du joueur {i+1} : ")     # saisir le nom de chaque joueur
    position = random.choice([3, 10, 17, 24])               # position de départ depuis une case relance
    plateau1.ajouter_joueur(Joueur(nom, position))          # 

os.system('clear')

joueurs = plateau1.joueurs                                  # stocker les joueurs 

for j in joueurs : 
    marche = True
    while marche : 
        print("-"*50, "TRIV-IA Pursuit", "-"*50)
        print(f"\nTour de {j.nom} !")
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
            print(f"Vous êtes tombé sur une case de thème {theme_case}")
            if case_joueur.est_case_camembert() and not j.camemberts[theme_case] : 
                print("⚠️   Tentez de gagner le camembert de ce thème   ⚠️")
                
            print(f"\nQuestion : {enonce} \n")                    # enoncé à l'indice 0
            for i,choix in enumerate(reponses) :                # choix à l'indice 1
                print(f"{i+1} - {choix}")                       # afficher tous les choix
            reponse_saisie = int(input("\nSaisissez le numéro de votre réponse : "))
            
            if reponses[reponse_saisie-1] == reponse_correcte : 

                if case_joueur.est_case_camembert() :           # si c'est une case camembert
                    if not j.camemberts[theme_case] :           # si le camembert du thème de la case n'est pas deja obtenu
                        j.ajouter_camembert(theme_case)         # ajout du camembert
                        print(f"Bravo vous venez de gagner le camembert du thème {theme_case}. Vous continuez à jouer ! ")
                else : 
                    print("Bonne réponse, vous continuez ! ")

            else : 
                print(f"Mauvaise réponse ! la réponse correcte était {reponse_correcte}")
                marche = False

        else  : 
            print("Vous êtes tombé sur une case relancer, vous allez rejouer ! \n")
        
        print("\n","-"*50)
        input()
        os.system('clear')
        plateau1.cases[position_apres_deplacement].joueur_dessus = False
    
    



