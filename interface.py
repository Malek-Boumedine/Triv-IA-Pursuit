import json
from tkinter import Canvas, mainloop, Tk
import time
import tkinter
import random

# dessiner un cercle dans un canvas
# le tag permet d'identifier le cercle dans le canvas 
def circle(canvas, x, y, r, width, name=""):
    return canvas.create_oval(x+r, y+r, x-r, y-r, width=width, tags=name)

# fun_tracage1 assure le calcul de l'ordonnée y du point central du cercle
# x : paramètre d'entrée qui représente l'abscisse du centre
# le calcul de la pente et du coefficient 
def fun_tracage1(pente, coeff, x)->int:
    return pente * x + coeff

# dessiner un texte dans un canvas
def text(canvas, x, y, text):
    return canvas.create_text(x, y, text=text, font=('bold', 8))

#préparation du canvas
window = Tk()
w = Canvas(window, width=1000, height=800, bg='white')

# le table de mappage permet de relier les informations fournies par le backend
# Il transforme le déplacement par des positions dans le canvas
# Il s'agit des positions des centres des différents cercles 
table_mappage ={}

# la case d'origine commence par le numero 100 dans la table de mappage
deplacement = 100
print(deplacement)

# dessine le jeu 
# les cases sous forme de cercle
# On dessine la structure et on charge la table de mappage
# TODO utiliser les cases internes
# Pour le moment on utlise que les cases externes
# ces cases sont présentées dans la table de mappage de l'indice 100 à 127
# le sens du montre dans le déplacement
# Garder les prints pour la vérification

def dessin():
    circle(w, 50, 300, 20, 3)
    #text(w, 50, 300, 'P0')
    table_mappage['114']=(50, 300)

    for i in range(100, 350, 50):
        circle(w, i, 300, 10, 3)
        #text(w, i, 300, 'P')
        #print(i)
    table_mappage['052']=(100, 300)
    table_mappage['042']=(150, 300)
    table_mappage['032']=(200, 300)
    table_mappage['022']=(250, 300)
    table_mappage['012']=(300, 300)

    circle(w, 350, 300, 20, 3)
    #table_mappage['000']=(350, 300)
    #abs, ord = table_mappage['000']
    #text(w, ord, abs, 'P')

    for i in range(400, 650, 50):
        circle(w, i, 300, 10, 3)
        #print(i)

    table_mappage['010']=(400, 300)
    table_mappage['020']=(450, 300)
    table_mappage['030']=(500, 300)
    table_mappage['040']=(550, 300)
    table_mappage['050']=(600, 300)

    circle(w, 650, 300, 20, 3)
    table_mappage['100']=(650, 300)

    for i in range(350, 600, 50):
        circle(w, 350, i, 10, 3)
        #print(i)

    table_mappage['011']=(350, 350)
    table_mappage['021']=(350, 400)
    table_mappage['031']=(350, 450)
    table_mappage['041']=(350, 500)
    table_mappage['051']=(350, 550)

    circle(w, 350, 600, 20, 3)
    table_mappage['107']=(350, 600) 

    for i in range(50, 300, 50):
        circle(w, 350, i, 10, 3)
        #print(i)
    table_mappage['053']=(350, 50)
    table_mappage['043']=(350, 100)
    table_mappage['033']=(350, 150)
    table_mappage['023']=(350, 200)
    table_mappage['013']=(350, 250)

    circle(w, 350, 0, 20, 3)
    table_mappage['121']=(350, 0)

    for i in range(400, 601, 40):
        circle(w, i, fun_tracage1(1, -350, i), 10, 3)
        #print(i," ", fun_tracage1(1, -350, i))

    table_mappage['122']=(400, 50)   
    table_mappage['123']=(440, 90)  
    table_mappage['124']=(480, 130)   
    table_mappage['125']=(520, 170)   
    table_mappage['126']=(560, 210)   
    table_mappage['127']=(600, 250)   

    print("###")

    for i in range(390, 601, 40):
        circle(w, i, fun_tracage1(-1, 950, i), 10, 3)
        #print(i," ", fun_tracage1(-1, 950, i))

    table_mappage['106']=(390, 560)   
    table_mappage['105']=(430, 520)   
    table_mappage['104']=(470, 480)   
    table_mappage['103']=(510, 440)   
    table_mappage['102']=(550, 400)   
    table_mappage['101']=(590, 360)   

    print("###")

    for i in range(100, 301, 40):
        circle(w, i, fun_tracage1(1, 250, i), 10, 3)
        #print(i," ", fun_tracage1(1, 250, i))

    table_mappage['113']=(100, 350)   
    table_mappage['112']=(140, 390)   
    table_mappage['111']=(180, 430)   
    table_mappage['110']=(220, 470)   
    table_mappage['109']=(260, 510)   
    table_mappage['108']=(300, 550)  
    print("###")

    for i in range(100, 301, 40):
        circle(w, i, fun_tracage1(-1, 350, i), 10, 3)
        #print(i," ", fun_tracage1(-1, 350, i))

    table_mappage['120']=(290, 60)  
    table_mappage['119']=(250, 100)   
    table_mappage['118']=(210, 140)   
    table_mappage['117']=(170, 180)   
    table_mappage['116']=(130, 220)   
    table_mappage['115']=(100, 260)   

    print("##########")

    # utilisation du pack pour l'organisation des cercles
    w.pack()
    time.sleep(2)

# chargement des questions depuis le fichier json
def chargement_question():
    with open ("liste_questions.json", "r") as file:
        data = json.load(file)
    question1 = list(data[0]["theme1"].keys())[0]
    return question1

# ajouter les différents boutons et labels dans l'interface principale
def bouton():
    
    global jouer, lancer, valider, resultat
    global a
    
    #a = random.randint(1,6)
    question = chargement_question()
   
    #label résultat du dé
    resultat = tkinter.Label(window, font =("Arial", 12, "bold"), bd=5, text = "Le résultat du dé est : ")
    #bouton jouer
    jouer = tkinter.Button(window,text= "Jouer", bg = "blue", fg = "white", font =("Arial", 12, "bold"), relief="raised", bd=5, state = "normal", command = clicbutton )
    #label de la question
    question = tkinter.Label(window, font =("Arial", 12, "bold"), bd=5, text = "La question est : "+question )
    #input de la réponse
    reponse = tkinter.Entry(window, font=("Arial", 12), fg="blue")
    #bouton valider
    valider = tkinter.Button(window,text = "Valider la réponse", bg = "blue", fg = "white", font =("Arial", 12, "bold"), relief="raised",state = "disable", bd=5)

    # utilisation du pack pour l'organisation des boutons et labels
    resultat.pack()
    jouer.pack()
    question.pack()
    reponse.pack()
    valider.pack()

    return jouer, valider, resultat

#activer le bouton jouer
def activer_ok():
    jouer.config(state = "normal")

#activation des boutons
def active_de():
    print("de active") 
    pas = random.randint(1,6)
    resultat.config(text="Le résultat du dé est : " + str(pas))
    etat = lancer.cget("state")
    if etat == "normal":
        jouer.config(state = "normal") 
    else:
        jouer.config(state = "disabled") 
    
    return  pas

# mouvement représente le déplacement dans le jeu
def mouvement():
    c = random.randint(1,6)
    print(c)
    global deplacement
    deplacement += c
    if deplacement >= 128:
        deplacement = 100
    return deplacement, c

# afficher le cercle qui représente le déplacement
def clicbutton():
    etat = jouer.cget("state")
    if etat == "normal":
        valider.config(state = "normal")
        jouer.config(state="disabled")
    w.delete("de")
    w.update()
    deplacer, pas = mouvement()
    abso, ordo = table_mappage[str(deplacer)]
    resultat.config(text="Le résultat du dé est : " + str(pas))
    print(f"ok {abso}")
    circlee = circle(w, abso, ordo, 5, 10, "de")
    w.pack()
    w.update()

#appel des différentes méthodes
dessin()
bouton()
mainloop()