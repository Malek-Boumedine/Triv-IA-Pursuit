import tkinter as tk

# Création de la fenêtre principale
window = tk.Tk()
window.title("Lancer le dé")
window.geometry("300x200")

# Fonction appelée lorsqu'on clique sur le bouton
def lancer_de():
    print("Le dé est lancé !")

# Configuration des couleurs au survol
def on_enter(e):
    lancer.config(bg="lightblue")

def on_leave(e):
    lancer.config(bg="blue")

# Création du bouton avec des styles
lancer = tk.Button(
    window, 
    text="Lancer le dé", 
    bg="blue", 
    fg="white", 
    font=("Arial", 12, "bold"), 
    relief="raised", 
    bd=5,  # Épaisseur de la bordure
    command=lancer_de
)

# Liaison des événements de survol avec les fonctions
lancer.bind("<Enter>", on_enter)
lancer.bind("<Leave>", on_leave)

# Placement du bouton au centre
lancer.pack(pady=50)

# Boucle principale
window.mainloop()
