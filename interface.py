from tkinter import Canvas, mainloop, Tk
import time
import tkinter
import random

def circle(canvas, x, y, r, width):
    return canvas.create_oval(x+r, y+r, x-r, y-r, width=width)

def fun_tracage1(pente, coeff, x)->int:
    return pente * x + coeff

def text(canvas, x, y, text):
    return canvas.create_text(x, y, text=text, font=('bold', 8))

window = Tk()
w = Canvas(window, width=1000, height=800, bg='white')
table_mappage ={}

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
        print(i," ", fun_tracage1(1, -350, i))

    table_mappage['122']=(400, 50)   
    table_mappage['123']=(440, 90)  
    table_mappage['124']=(480, 130)   
    table_mappage['125']=(520, 170)   
    table_mappage['126']=(560, 210)   
    table_mappage['127']=(600, 250)   

    print("###")

    for i in range(390, 601, 40):
        circle(w, i, fun_tracage1(-1, 950, i), 10, 3)
        print(i," ", fun_tracage1(-1, 950, i))

    table_mappage['106']=(390, 560)   
    table_mappage['105']=(430, 520)   
    table_mappage['104']=(470, 480)   
    table_mappage['103']=(510, 440)   
    table_mappage['102']=(550, 400)   
    table_mappage['101']=(590, 360)   

    print("###")

    for i in range(100, 301, 40):
        circle(w, i, fun_tracage1(1, 250, i), 10, 3)
        print(i," ", fun_tracage1(1, 250, i))

    table_mappage['113']=(100, 350)   
    table_mappage['112']=(140, 390)   
    table_mappage['111']=(180, 430)   
    table_mappage['110']=(220, 470)   
    table_mappage['109']=(260, 510)   
    table_mappage['108']=(300, 550)  
    print("###")

    for i in range(100, 301, 40):
        circle(w, i, fun_tracage1(-1, 350, i), 10, 3)
        print(i," ", fun_tracage1(-1, 350, i))

    table_mappage['120']=(290, 60)  
    table_mappage['119']=(250, 100)   
    table_mappage['118']=(210, 140)   
    table_mappage['117']=(170, 180)   
    table_mappage['116']=(130, 220)   
    table_mappage['115']=(100, 260)   

    print("##########")

    w.pack()
    time.sleep(2)



def bouton():
    

    global jouer
    global a


    a = random.randint(1,6)

    lancer = tkinter.Button(window,text= "Lancer le dé", bg = "blue", fg = "white", font =("Arial", 12, "bold"), relief="raised", bd=5, command = activer_ok)
    resultat = tkinter.Label(window, font =("Arial", 12, "bold"), bd=5, text = "Le résultat du dé est : " + str(a))
    jouer = tkinter.Button(window,text= "Jouer", bg = "blue", fg = "white", font =("Arial", 12, "bold"), relief="raised", bd=5, state = "disable")
    question = tkinter.Label(window, font =("Arial", 12, "bold"), bd=5, text = "La question est : ")
    reponse = tkinter.Entry(window, font=("Arial", 12), fg="blue")
    valider = tkinter.Button(window,text = "Valider la réponse", bg = "blue", fg = "white", font =("Arial", 12, "bold"), relief="raised", bd=5)

    lancer.pack()
    resultat.pack()
    jouer.pack()
    question.pack()
    reponse.pack()
    valider.pack()

    return lancer, jouer

def activer_ok():
    jouer.config(state = "normal")
    

def mouvement():
    """
    a chaque click Jouer  : déplacement aleatoire en fonction "a" dans table_mappage
    
    
    """
    while jouer :
        deplacement = 100 + int(a)
        return deplacement
    

        


dessin()

deplacement = range(100, 128)
# print(table_mappage)
bouton()
# activer_ok()

for param in deplacement:



    # abso, ordo = table_mappage[str(param)]
    abso, ordo = table_mappage[str(mouvement())]


    print(f"ok {abso}")
    circlee = circle(w, abso, ordo, 5, 10)
    w.pack()
    w.update()
    time.sleep(1)
    w.delete(circlee)
    w.update()


mainloop()