class Case:
    TYPES_CASES = ["camembert", "relance", "normale"]
    rouge, vert, jaune, bleu, magenta, marron, default = "\033[91m", "\033[92m", "\033[93m", '\033[94m', '\033[35m', '\033[33m', '\033[99m'

    
    def __init__(self, type_case : str, coordonnees : int, theme : str, couleur : str, joueur_dessus : bool = False):
        self.type_case = type_case      # [camembert, relance, normale]
        self.coordonnees = coordonnees  # [anneau, position, rayon] comme dans la classe joueur
        self.theme = theme              # [4 thèmes à définir avec l'équipe]
        self.couleur = couleur          # couleur du thème a définir (en hexa ???)
        self.joueur_dessus = joueur_dessus

    def est_case_camembert(self) -> bool:
        return self.type_case == "camembert"

    def est_case_relance(self) -> bool:
        return self.type_case == "relance"

    def est_case_normale(self) -> bool:
        return self.type_case == "normale"

    def obtenir_theme(self) -> str:
        return self.theme

    def obtenir_position(self) :
        return self.coordonnees
    
    def obtenir_couleur(self) : 
        return self.couleur
    
    def __str__(self):
        if self.type_case == "relance":
            return f"\033[37m▼▼{Case.default}" if self.joueur_dessus else "🎲"
        else : 
            if self.couleur == Case.rouge : 
                return f"\033[91m▼▼{Case.default}" if self.joueur_dessus else "🟥"
            elif self.couleur == Case.vert : 
                return f"\033[92m▼▼{Case.default}" if self.joueur_dessus else "🟩"
            elif self.couleur == Case.jaune : 
                return f"\033[93m▼▼{Case.default}" if self.joueur_dessus else "🟨"
            elif self.couleur == Case.bleu : 
                return f"\033[94m▼▼{Case.default}" if self.joueur_dessus else "🟦"
            elif self.couleur == Case.magenta : 
                return f"\033[35m▼▼{Case.default}" if self.joueur_dessus else "🟪"
            elif self.couleur == Case.marron : 
                return f"\033[33m▼▼{Case.default}" if self.joueur_dessus else "🟫"
            else: 
                return


# print("\033[37mTexte en blanc\033[0m")
# print("\033[90mTexte en gris clair\033[0m")