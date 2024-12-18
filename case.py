class Case:
    TYPES_CASES = ["camembert", "relance", "normale"]
    
    def __init__(self, type_case : str, coordonnees : int, theme : str, couleur : str):
        self.type_case = type_case      # [camembert, relance, normale]
        self.coordonnees = coordonnees  # [anneau, position, rayon] comme dans la classe joueur
        self.theme = theme              # [4 thèmes à définir avec l'équipe]
        self.couleur = couleur          # couleur du thème a définir (en hexa ???)

    def est_case_camembert(self) -> bool:
        return self.type_case == "camembert"

    def est_case_relance(self) -> bool:
        return self.type_case == "relance"

    def est_case_normale(self) -> bool:
        return self.type_case == "normale"

    def obtenir_theme(self) -> str:
        return self.theme if self.est_case_camembert() else None

    def obtenir_position(self) -> list[int]:
        return self.coordonnees
    
    def obtenir_couleur(self) : 
        return self.couleur
    


############################################################

if __name__ == "__main__" : 
    case_camembert = Case("camembert", [1, 7, 1], "T1")  
    case_relance = Case("relance", [1, 3, 0], None)      
    case_normale = Case("normale", [0, 2, 3], None)      
    case_centre = Case("normale", [0, 0, 0], None)       




