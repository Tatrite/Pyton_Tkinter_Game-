# Créé par flofu, le 06/12/2022 en Python 3.7
# Utilisation des listes et de la fonction after
from tkinter import *

def anim():
    global x, indice, Fichier
    x = x + 10
    if x > 1000 :
        x = 0

    indice = indice + 1
    if indice == 4 :
        indice = 0

    Fond.itemconfig(Matt, image = Fichier[indice]) # Change l'image
    Fond.coords(Matt, x, 10) # Change les coordonnées de l'image

    fenetre.after(50, anim) # Rappel de la fonction anim() toutes les 150 ms

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Le marcheur")

# Création du Canevas
Fond = Canvas(fenetre, width=1000, height=18, bg="white")
Fond.pack()

# importation des 8 images
To=["G","D","H","B"]
Fichier=[]
for e in To:
        Fichier.append(PhotoImage(file="Balle" + e + ".png"))

x, indice = 0, 0
Matt = Fond.create_image(x, 0, image=Fichier[indice], anchor='nw')

anim()

# Lancement de l'interface graphique
fenetre.mainloop()
