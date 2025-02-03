# Créé par flofu, le 15/11/2022 en Python 3.7
from tkinter import*
def charge_labyrinthe(nom):
    """
    Charge le labyrinthe depuis le fichier nom.txt

    nom : Nom du fichier contenant le labyrinthe (sans l'extension .txt)

    Valeur de retour : Liste contenant les données du labyrinthe
    """
    fic = open(nom + ".txt", "rt")
    data = fic.readlines()
    fic.close()

    for i in range(len(data)):
        data[i] = data[i].rstrip()
    print('Vous ête tomber sur le labyrinte:'+nom)

    return data

def charge_fichier():
    Fichier = []
    M=["G","H","D","B","Hf","Gf","C"]
    Tcoords=[]
    for e in M:
        Fichier.append(PhotoImage(file="mure" + e + ".png"))
    C=["BG","HD","HG","BD"]
    for e in C:
        Fichier.append(PhotoImage(file="coin" + e + ".png"))
    T=["G","D","H","B","M"]
    for e in T:
        Fichier.append(PhotoImage(file="TANK" + e + ".png"))
    To=["G","D","H","B"]
    for e in To:
        Fichier.append(PhotoImage(file="Tourelle" + e + ".png"))
    Fichier.append(PhotoImage(file="New Piskel (1).png"))
    Fichier.append(PhotoImage(file="New Piskel.png"))
    Tb=["G","D","H","B"]
    for e in Tb:
        Fichier.append(PhotoImage(file="Balle" + e + ".png"))
    Fichier.append(PhotoImage(file="nVie.png"))
    Fichier.append(PhotoImage(file="Vie.png"))
    Fichier.append(PhotoImage(file="Boost.png"))
    Fichier.append(PhotoImage(file="QG.png"))
    Fichier.append(PhotoImage(file="herbe.png"))
    Fichier.append(PhotoImage(file="sole.png"))
    Fichier.append(PhotoImage(file="sable.png"))
    return Fichier
