import random


class Joueur:
    def __init__(self, nom: str):
        self.nom = nom
        self.position = [0, 0, 0]  # [anneau, position, rayon],  anneau 0=rayons - 1=cercle extérieur, rayon 0=centre - rayon 1à6=rayons
        self.camembert_entier = False
        self.camemberts = {
            "T1": False,
            "T2": False,
            "T3": False,
            "T4": False,
            "T5": False,
            "T6": False
        }

    def lancer_de(self) -> int :
        return random.randint(1, 6)

    def se_deplacer(self) -> None :
        input("Appuyez sur Entree pour lancer le dé !")
        resultat_de = self.lancer_de()
        print(f"{self.nom} a obtenu un {resultat_de} au lancé de dé !")

        if self.position[0] == 1 :  # Sur le cercle extérieur
            # gérer le cas ou on est sur une case de camembert pour se déscendre sur la colonne
            # gérer le cas ou c'est une case relancer dé    -> recursivité se_deplacer()
            #
            choix = input("Voulez-vous aller à droite (D) ou à gauche (G)? ").upper()        # modifier plus tard pour proposer la case sur laquelle se déplacer (en fonction du thème)
            if choix == 'D' :
                self.position[1] = (self.position[1] + resultat_de) % 42    # comme dans wator pour gérer le mvt toroidal
            else :
                self.position[1] = (self.position[1] - resultat_de) % 42
        
        else :  # Sur un rayon ou au centre
            if self.position[1] == 0 and self.position[2] == 0 :  # Au centre
                # choisir une colonne, pour le moment juste saisir numéro de colonne, par la suite proposer la colonne en fonction du thème de la case correspondant au lancé de dé
                num_colonne = int(input("Veuiller choisir un nombre entre 0 et 5"))
                if resultat_de == 6 :
                    self.position[0] = 1                        # il passe au cercle extérieur
                    self.position[1] = num_colonne * 7          # il passe directement sur l'une des cases contenant un triangle camembert
                    self.position[2] = num_colonne              # numéro de colonne
                else :
                    self.position[1] = resultat_de              # il se déplace sur la colonne qu'il a choisi
                    self.position[2] = num_colonne              # numéro de colonne cjhoisie 
            else :   # sur un rayon
                distance_bord = 6 - self.position[1]            # distance restante pour arriver au bord
                if resultat_de == distance_bord :
                    # ajouter ici une logique pour choisir d'aller vers la case du bord ou revenir en arrière (optionnel ???)
                    self.position[0] = 1                        # Passe sur le cercle extérieur
                    self.position[1] = self.position[2] * 7     # x 7 car on a 42 cases pour 6 rayons ou thèmes (42 / 6 = 7)
                elif resultat_de > distance_bord :
                    self.position[0] = 1                        # Passe sur le cercle extérieur
                    choix = input("Voulez-vous aller à droite (D) ou à gauche (G)? ").upper()   # modifier plus tard pour proposer la case sur laquelle se déplacer (en fonction du thème)
                    deplacement_restant = resultat_de - distance_bord
                    if choix == 'D':        # pareil ici à modifier plus tard pour proposer les cases correspondant aux mvts possibles
                        self.position[1] = (self.position[2] * 7 + deplacement_restant) % 42    # le modulo 42 pour ne pas déborder au dela des 42 cases, pour reproduire le mouvement circulaire
                    else :
                        self.position[1] = (self.position[2] * 7 - deplacement_restant) % 42
                else :
                    self.position[1] += resultat_de



    #########################################################################################################
    
        
    def verifier_si_case_camembert(self) :  # vérifie si le joueur est sur une case camembert pour tenter de la gagner et l'ajouter à self.camemberts --> peut se faire avec la classe Case avec le type de case au lieu de cette méthode
        pass
                    
    def ajouter_camembert(self) :   # ajouer le camembert d'un thème à self.camemberts  --> si case de type camembert tenter de gagner le camembert du thème correspondant
        pass
    
    def afficher_camemberts(self) : # pour afficher les camemberts deja obtenus par le joueur
        pass
    
    def retour_centre(self) :       # retourner au centre pour tenter de gagner la partie si tous les camemberts ont été récoltés       OU retour avec les lancés de dé
        pass
    
    def poser_question_finale(self) : # poser la question finale au joueur lorsqu'il se retrouve sur le centre et qu'il a deja récolté les 6 camemberts
        pass        






        """

        COMMENT SE DÉPLACER
        SUR LE PLATEAU
        Au début de la partie, déplacez-vous en
        partant de la case centrale du plateau et en
        utilisant les « passerelles » pour vous rendre
        sur l’axe circulaire. Sur cet axe, vous pouvez
        vous déplacer dans n’importe quel sens.
        Essayez toujours de vous déplacer de telle
        manière que vous atterrissiez sur des cases
        dont le thème vous convient.
        Au cours d’un même déplacement, vous
        ne pouvez revenir sur vos pas. Par exemple,
        si vous faites 5, vous ne pouvez pas vous
        déplacer de 3 cases vers la gauche, vous
        arrêter et repartir de 2 cases vers la droite.
        En revanche, au prochain tour, vous pourrez
        changer de direction par rapport à votre
        déplacement précédent.
        Vous pouvez aussi utiliser les “passerelles”
        pour vous rendre plus rapidement de l’autre
        côté du plateau. Vous pouvez vous arrêter sur
        une case déjà occupée par un autre joueur.

        https://cdn.1j1ju.com/medias/d4/6f/18-trivial-pursuit-edition-famille-regle.pdf
       
        """
        
    

    









