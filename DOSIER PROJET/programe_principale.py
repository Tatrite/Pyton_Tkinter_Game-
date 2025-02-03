 # Créé par flofu, le 08/11/2022 en Python 3.7
from tkinter import*
from random import randint
from ProjetUnitéClasse import tank
from chargedoc import charge_labyrinthe,charge_fichier
from ProjetBallesClasse import balle
from ProjetBatimentClasse import Unite,QG
def tourelle_tir():
    # appele au fonction de tire des tourelles
    tirerT1()
    tirerT2()
    tirerT3()
    tirerT4()
    tirerT5()
    tirerT6()

def aficher_play_depuis_gameOver():
    global play
    play. pack_forget()
    Play=Button(Game_Over, width=8, height=2, text="PLAY |>", command = PdG)
    Play.place(x = 250, y = 300, anchor = "nw")


def aficher_play_depuis_Menu():
    global play
    play. pack_forget()
    Play=Button(Home, width=12, height=2, text="PLAY |>", command = PdM)
    Play.place(x = 60, y = 250, anchor = "nw")

def MdP():
    detruire_Plateau()
    create_menu()
def PdG():
    Game_Over.destroy()
    create_Plateau()
    tourelle_tir()
def PdM():
    #destruction du menu
    Home.destroy()
    create_Plateau()
    tourelle_tir()
def MdG():
    Game_Over.destroy()
    create_menu()
def anim_mort():
    global coc
    global mort; mort=1
    Fond.itemconfig(coc, image=Fichier[-12])
    fenetre.after(300, anim_mort2)
def anim_mort2():
    global coc
    global Tank
    global mort; mort=0
    Fond.itemconfig(coc, image=Fichier[-13])
    mat = Fond.create_image(Tank.x, Tank.y, image=Fichier[-13], anchor='nw')
    if Tank.nbvie>0:
        Fond.itemconfig(coc, image=Fichier[12])
        Tank.x,Tank.y=18,18
        Fond.coords(coc, Tank.x, Tank.y)


def game_over():
    global Game_Over
    global Tank
    global niv
    global score
    global F
    global play
    global Touréledétruite
    detruire_Plateau()
    Game_Over=Canvas(fenetre,width=360, height=360, bg="Black")
    Game_Over.pack()
    F=[]
    F.append(PhotoImage(file="Game_Over.png"))
    M = Game_Over.create_image(2, 2, image=F[0], anchor='nw')
    Quite=Button(Game_Over, width=7, height=1, text="QUITER X", command = destro)
    Quite.place(x = 362, y = 2, anchor = "ne")
    Menu=Button(Game_Over, width=8, height=2, text="MENU", command = MdG)
    Menu.place(x = 110, y = 300, anchor = "ne")
    if score ==0:
        S=Label(Game_Over,text='Patétique',bg="Black", fg='white')
    else:
        S=Label(Game_Over,text=str(score),bg="Black", fg='white')
    if score ==0:
        T=Label(Game_Over,text='NUL',bg="Black", fg='white')
    else:
        T=Label(Game_Over,text=str(Touréledétruite),bg="Black", fg='white')
    if score ==0:
        QG=Label(Game_Over,text='NUL',bg="Black", fg='white')
    else:
        QG=Label(Game_Over,text=str(niv-1),bg="Black", fg='white')
    if niv ==0:
        N=Label(Game_Over,text='But Nobody Came      =)',bg="Black", fg='white',font=("papyrus", 10))
    else:
        N=Label(Game_Over,text=str(niv),bg="Black", fg='white')
    S.place(x = 90, y = 130, anchor = "nw")
    T.place(x = 135, y = 160, anchor = "nw")
    N.place(x = 95, y = 230, anchor = "nw")
    QG.place(x = 135, y = 200, anchor = "nw")
    play=Button(Game_Over, width=8, height=2, text="PLAY |>")
    play.place(x = 250, y = 300, anchor = "nw")
    Tank=tank(18,18,10,4,25)
    niv=1
    score=0
    Tdétruite=0
    QGdétruite=0
    fenetre.after(1300, aficher_play_depuis_gameOver)

def nPlateau():
    global niv
    global Tank
    global Mode
    niv+=1
    r=randint(1,3)
    if r==1:
        Tank.augmenter_ap(1)
    elif r==2:
        Tank.augmenter_cp(1)
    elif r==3:
        Tank.augmenter_pv(1)
    detruire_Plateau()
    create_Plateau()

def destro():
    fenetre.destroy()

def detruire_Plateau():
    Fvie.destroy()
    Fstat.destroy()
    Fond.destroy()
def create_Plateau():
    global Fond
    global tir
    global Fvie
    global Fstat
    global Stat
    global Pv
    global Ataque
    global Défence
    global nv
    global scr
    global Home
    global Quit
    global vie
    global vie2
    global vie3
    global vieco
    global vieco2
    global vieco3
    global coc
    global Viecoord
    global Tcoords
    global Mure
    global QGcoords
    global Bcoorgs
    global Tank
    global B
    global T1
    global T1I
    global T2
    global T2I
    global T3
    global T3I
    global T4
    global T4I
    global T5
    global T5I
    global T6
    global T6I
    global mort
    global Qg
    global Touréledétruite
    global jouer
    jouer=True
    tir=False
    Viecoord=[]
    Tcoords=[]
    Mure=[]
    QGcoords=[]
    Bcoorgs=[]
    mort=0
    Touréledétruite=0
    #création de la carte
    Fond = Canvas(fenetre, width=360, height=360, bg="white")
    Fvie= Frame(fenetre, width=100, height=18, bg="Blue")
    Fstat= Frame(fenetre, width=360, height=60, bg="Blue")
    Quit=Button(Fstat, width=2, height=1, text="X", command = destro)
    Menu=Button(Fstat, width=4, height=1, text="Menu",command = MdP)
    Stat = Canvas(Fstat, width=268, height=52, bg="Red")
    Pv=Label(Stat,text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
    Ataque=Label(Stat,text='Attaque:'+str(Tank.cp+Tank.cpboost))
    Défence=Label(Stat,text='Defence:'+str(Tank.ap+Tank.apboost))
    nv=Label(Stat,text='Niveau:'+str(niv))
    scr=Label(Stat,text='Score:'+str(score))
    #affichage des states
    Fvie.place(x = 10, y = 10, anchor = "se")
    Fstat.pack()
    Quit.pack(side="right")
    Menu.pack(side="right")
    Stat.pack(side="left")
    Pv.pack(side="left")
    Ataque.pack(side="left")
    Défence.pack(side="left")
    nv.pack(side="left")
    scr.pack(side="left")
    #affichage et génération du Terrain de jeux
    Fond.pack()
    niveau=randint(1,100)
    if niveau==100:
      niveau=randint(1,2)
      data=charge_labyrinthe("sp"+str(niveau))
    else:
        niveau=randint(1,4)
        data=charge_labyrinthe(str(niveau))
    affiche_cart(data,Fichier)
    #Affichage des point de heal
    vie = Fond.create_image(Viecoord[0][0], Viecoord[0][1], image=Fichier[-6], anchor='nw')
    vieco=Viecoord[0]
    vie2 = Fond.create_image(Viecoord[1][0], Viecoord[1][1], image=Fichier[-6], anchor='nw')
    vieco2=Viecoord[1]
    vie3= Fond.create_image(Viecoord[2][0], Viecoord[2][1], image=Fichier[-6], anchor='nw')
    vieco3=Viecoord[2]
    #Affichage des tourelle
    T1=Unite(Tcoords[0][0],Tcoords[0][1],10,5,1)
    T1I = Fond.create_image(T1.x, T1.y, image=Fichier[16], anchor='nw')
    T2=Unite(Tcoords[1][0],Tcoords[1][1],10,5,1)
    T2I = Fond.create_image(T2.x, T2.y, image=Fichier[16], anchor='nw')
    T3=Unite(Tcoords[2][0],Tcoords[2][1],10,5,1)
    T3I = Fond.create_image(T3.x, T3.y, image=Fichier[16], anchor='nw')
    T4=Unite(Tcoords[3][0],Tcoords[3][1],10,5,1)
    T4I = Fond.create_image(T4.x, T4.y, image=Fichier[16], anchor='nw')
    T5=Unite(Tcoords[4][0],Tcoords[4][1],10,5,1)
    T5I = Fond.create_image(T5.x, T5.y, image=Fichier[16], anchor='nw')
    T6=Unite(Tcoords[5][0],Tcoords[5][1],10,5,1)
    T6I = Fond.create_image(T6.x, T6.y, image=Fichier[16], anchor='nw')

    #affichage de la base enemie
    Qg=QG(QGcoords[0],QGcoords[1],50)
    QGI = Fond.create_image(Qg.x, Qg.y, image=Fichier[-4], anchor='nw')

    #affichage du Tank
    Tank.x=18
    Tank.y=18
    coc= Fond.create_image(Tank.x, Tank.y, image=Fichier[12],anchor='nw')

    # Ajout des surveillances des touches pour le déplacement et pour tirer
    fenetre.bind_all('<Up>', Tirehaut)
    fenetre.bind_all('<Down>', Tirebas)
    fenetre.bind_all('<Right>', Tiredroite)
    fenetre.bind_all('<Left>', Tiregauche)
    fenetre.bind_all('<Z>', haut)
    fenetre.bind_all('<S>', bas)
    fenetre.bind_all('<D>', droite)
    fenetre.bind_all('<Q>', gauche)
    fenetre.bind_all('<z>', haut)
    fenetre.bind_all('<s>', bas)
    fenetre.bind_all('<d>', droite)
    fenetre.bind_all('<q>', gauche)

def create_menu():
    global Fvie
    global Fstat
    global Fond
    global Home
    global Tank
    global niv
    global score
    global F
    global play
    Tank=tank(18,18,10,4,25)
    niv=1
    score=0
    #création et afichage du menue
    Home=Canvas(fenetre,width=360, height=360, bg="Red")
    Home.pack()
    F=[]
    F.append(PhotoImage(file="écran_titre.png"))
    M = Home.create_image(2, 2, image=F[0], anchor='nw')
    Quit=Button(Home, width=6, height=1, text="Quiter X", command = destro)
    Quit.place(x = 365, y = 0, anchor = "ne")
    play=Button(Home, width=12, height=2, text="PLAY |>")
    play.place(x = 60, y = 250, anchor = "nw")
    fenetre.after(1300, aficher_play_depuis_Menu)
#------------------------ --------------------------------------------
# Définition des fonctions appelées lors de l'appui sur les touche Z,Q,S,D
def haut(evt):
    global Tank
    global cdD
    global mort
    if cdD!=1 and mort==0:
        coul_downD()
        Fond.itemconfig(coc, image=Fichier[13])
        Tank.direct="H"
        Tank.y-=18
        if not(Tank.x, Tank.y) in Mure and (Tank.x, Tank.y) != QGcoords:
            Fond.coords(coc, Tank.x, Tank.y)
            if (Tank.x, Tank.y) in Bcoorgs:
                Tank.cpboost=2
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
            else:
                Tank.cpboost=0
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
            if (Tank.x, Tank.y) in Viecoord:
                Viecoord.remove((Tank.x, Tank.y))
                if (Tank.x, Tank.y)==vieco:
                    Fond.itemconfig(vie, image=Fichier[-7])
                if (Tank.x, Tank.y)==vieco2:
                    Fond.itemconfig(vie2, image=Fichier[-7])
                if (Tank.x, Tank.y)==vieco3:
                    Fond.itemconfig(vie3, image=Fichier[-7])
                Tank.reparer(2)
                Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
        else:
            Tank.y+=18
def bas(evt):
    global Tank
    global cdD
    global mort
    if cdD!=1 and mort==0:
        coul_downD()
        Fond.itemconfig(coc, image=Fichier[14])
        Tank.direct="B"
        Tank.y+=18
        if not(Tank.x, Tank.y) in Mure and (Tank.x, Tank.y) != QGcoords:
            Fond.coords(coc, Tank.x, Tank.y)
            if (Tank.x, Tank.y) in Bcoorgs:
                Tank.cpboost=2
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
            else:
                Tank.cpboost=0
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
            if (Tank.x, Tank.y) in Viecoord:
                Viecoord.remove((Tank.x, Tank.y))
                if (Tank.x, Tank.y)==vieco:
                    Fond.itemconfig(vie, image=Fichier[-7])
                if (Tank.x, Tank.y)==vieco2:
                    Fond.itemconfig(vie2, image=Fichier[-7])
                if (Tank.x, Tank.y)==vieco3:
                    Fond.itemconfig(vie3, image=Fichier[-7])
                Tank.reparer(2)
                Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
        else:
            Tank.y-=18
def gauche(evt):
    global Tank
    global cdD
    global mort
    if cdD!=1 and mort==0:
        coul_downD()
        Fond.itemconfig(coc, image=Fichier[11])
        Tank.direct="G"
        Tank.x-=18
        if not(Tank.x, Tank.y) in Mure and (Tank.x, Tank.y) != QGcoords:
            Fond.coords(coc, Tank.x, Tank.y)
            if (Tank.x, Tank.y) in Bcoorgs:
                Tank.cpboost=2
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
            else:
                Tank.cpboost=0
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
            if (Tank.x, Tank.y) in Viecoord:
                Viecoord.remove((Tank.x, Tank.y))
                if (Tank.x, Tank.y)==vieco:
                    Fond.itemconfig(vie, image=Fichier[-7])
                if (Tank.x, Tank.y)==vieco2:
                    Fond.itemconfig(vie2, image=Fichier[-7])
                if (Tank.x, Tank.y)==vieco3:
                    Fond.itemconfig(vie3, image=Fichier[-7])
                Tank.reparer(2)
                Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
        else:
            Tank.x+=18


def droite(evt):
    global Tank
    global cdD
    global mort
    if cdD!=1 and mort==0:
        coul_downD()
        Fond.itemconfig(coc, image=Fichier[12])
        Tank.direct="D"
        Tank.x+=18
        if not(Tank.x, Tank.y) in Mure and (Tank.x, Tank.y) != QGcoords:
            Fond.coords(coc, Tank.x, Tank.y)
            if (Tank.x, Tank.y) in Bcoorgs:
                Tank.cpboost=2
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
            else:
                Tank.cpboost=0
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
            if (Tank.x, Tank.y) in Viecoord:
                Viecoord.remove((Tank.x, Tank.y))
                if (Tank.x, Tank.y)==vieco:
                    Fond.itemconfig(vie, image=Fichier[-7])
                if (Tank.x, Tank.y)==vieco2:
                    Fond.itemconfig(vie2, image=Fichier[-7])
                if (Tank.x, Tank.y)==vieco3:
                    Fond.itemconfig(vie3, image=Fichier[-7])
                Tank.reparer(2)
                Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
        else:
            Tank.x-=18


def coul_downD():
    global cdD
    if cdD!=1:
        cdD=1
        fenetre.after(250, coul_downD2)
def coul_downD2():
    global cdD
    cdD=0

#--------------------------------------------------------------------
#fonction de tire (Fléche directionelle)
def Tirehaut(evt):
    global cd
    global  tir
    global Tank
    global mort
    if cd!=1 and not tir and not mort:
        coul_down()
        Fond.itemconfig(coc, image=Fichier[13])
        Tank.direct='H'
        tirer()
def Tirebas(evt):
    global cd
    global  tir
    global Tank
    global mort
    if cd!=1 and not tir and not mort:
        coul_down()
        Fond.itemconfig(coc, image=Fichier[14])
        Tank.direct='B'
        tirer()
def Tiredroite(evt):
    global cd
    global  tir
    global Tank
    global mort
    if cd!=1 and not tir and not mort:
        coul_down()
        Fond.itemconfig(coc, image=Fichier[12])
        Tank.direct='D'
        tirer()
def Tiregauche(evt):
    global cd
    global  tir
    global Tank
    global mort
    if cd!=1 and not tir and not mort:
        coul_down()
        Fond.itemconfig(coc, image=Fichier[11])
        Tank.direct='G'
        tirer()

def tirer():
    global Tank
    global B
    global Balle
    global tir
    tir=True
    Balle=balle(Tank.x,Tank.y,Tank.attaquer(),Tank.direct)
    if Balle.direct=="H":
        B=Fond.create_image(Balle.x+7, Balle.y+7, image=Fichier[-9], anchor='nw')
    if Balle.direct=="B":
        B=Fond.create_image(Balle.x+7, Balle.y+7, image=Fichier[-8], anchor='nw')
    if Balle.direct=="G":
        B=Fond.create_image(Balle.x+7, Balle.y+7, image=Fichier[-11], anchor='nw')
    if Balle.direct=="D":
        B=Fond.create_image(Balle.x+7, Balle.y+7, image=Fichier[-10], anchor='nw')

    rec_tirer()

def coul_down():
    global cd
    if cd!=1:
        cd=1
        fenetre.after(750, coul_down2)
def coul_down2():
    global cd
    cd=0

def rec_tirer():
    global B
    global Balle
    global tir
    global T1
    global T1I
    global T2
    global T2I
    global T3
    global T3I
    global T4
    global T4I
    global T5
    global T5I
    global T6
    global T6I
    global Touréledétruite
    global Qg
    global score
    if not (Balle.x,Balle.y)in Mure and not (Balle.x,Balle.y)in Tcoords and not (Balle.x,Balle.y)== QGcoords:
        if Balle.direct=="B":
                Balle.Desendre(18)
        if Balle.direct=="H":
                Balle.Monte(18)
        if Balle.direct=="D":
                Balle.Droite(18)
        if Balle.direct=="G":
                Balle.Gauche(18)
        Fond.coords(B,Balle.x+7, Balle.y+7)
        fenetre.after(20,rec_tirer)
    else:
        Fond.delete(B)
        tir=False
        if (Balle.x,Balle.y)==(T1.x,T1.y):
            T1.subir_degats(Balle.dégat)
            if T1.détruite==True:
                Fond.delete(T1I)
                Touréledétruite+=1
                score+=1
                Ataque.configure(text='Ataque:'+str(Tank.cp+Tank.cpboost))
                scr.configure(text='Score:'+str(score))
        elif (Balle.x,Balle.y)==(T2.x,T2.y):
            T2.subir_degats(Balle.dégat)
            if T2.détruite==True:
                Fond.delete(T2I)
                Touréledétruite+=1
                score+=1
                scr.configure(text='Score:'+str(score))
        elif (Balle.x,Balle.y)==(T3.x,T3.y):
            T3.subir_degats(Balle.dégat)
            if T3.détruite==True:
                Fond.delete(T3I)
                Touréledétruite+=1
                score+=1
                scr.configure(text='Score:'+str(score))
        elif (Balle.x,Balle.y)==(T4.x,T4.y):
            T4.subir_degats(Balle.dégat)
            if T4.détruite==True:
                Fond.delete(T4I)
                Touréledétruite+=1
                score+=1
                scr.configure(text='Score:'+str(score))
        elif (Balle.x,Balle.y)==(T5.x,T5.y):
            T5.subir_degats(Balle.dégat)
            if T5.détruite==True:
                Fond.delete(T5I)
                Touréledétruite+=1
                score+=1
                scr.configure(text='Score:'+str(score))
        elif (Balle.x,Balle.y)==(T6.x,T6.y):
            T6.subir_degats(Balle.dégat)
            if T6.détruite==True:
                Fond.delete(T6I)
                Touréledétruite+=1
                score+=1
                scr.configure(text='Score:'+str(score))
        elif (Balle.x,Balle.y)== QGcoords and Touréledétruite >=6:
            Qg.subir_degats(Balle.dégat)
            print(Qg.pv)
            print(Qg.détruite)
            if Qg.détruite==True:
                score+=10
                nPlateau()


#--------------------------------------------------------------------
#fonction de tire de la tourelle1
def tirerT1():
    global T1
    global Tank
    global BT1
    global BalleT1
    if T1.x<Tank.x:
        T1.direct="D"
        Fond.itemconfig(T1I, image=Fichier[17])
    elif T1.x>Tank.x:
        T1.direct="G"
        Fond.itemconfig(T1I, image=Fichier[16])
    elif T1.y>Tank.y:
        T1.direct="H"
        Fond.itemconfig(T1I, image=Fichier[18])
    elif T1.y<Tank.y:
        T1.direct="B"
        Fond.itemconfig(T1I, image=Fichier[19])
    BalleT1=balle(T1.x,T1.y,T1.attaquer(),T1.direct)
    if BalleT1.direct=="H":
        BT1=Fond.create_image(BalleT1.x+7, BalleT1.y+7, image=Fichier[-9], anchor='nw')
    if BalleT1.direct=="B":
        BT1=Fond.create_image(BalleT1.x+7, BalleT1.y+7, image=Fichier[-8], anchor='nw')
    if BalleT1.direct=="G":
        BT1=Fond.create_image(BalleT1.x+7, BalleT1.y+7, image=Fichier[-11], anchor='nw')
    if BalleT1.direct=="D":
        BT1=Fond.create_image(BalleT1.x+7, BalleT1.y+7, image=Fichier[-10], anchor='nw')

    rec_tirerT1()

def rec_tirerT1():
    global BT1
    global BalleT1
    global Tank
    global Pv
    if not (BalleT1.x,BalleT1.y)in Mure and (BalleT1.x,BalleT1.y)!=(Tank.x,Tank.y):
        if BalleT1.direct=="B":
                BalleT1.Desendre(18)
        if BalleT1.direct=="H":
                BalleT1.Monte(18)
        if BalleT1.direct=="D":
                BalleT1.Droite(18)
        if BalleT1.direct=="G":
                BalleT1.Gauche(18)
        Fond.coords(BT1,BalleT1.x+7, BalleT1.y+7)
        fenetre.after(20,rec_tirerT1)
    else:
        if (BalleT1.x,BalleT1.y)==(Tank.x,Tank.y):
            vie1=Tank.nbvie
            Tank.subir_degats(BalleT1.dégat)
            Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
            if vie1!=Tank.nbvie:
                anim_mort()
                if Tank.détruite:
                    fenetre.after(600,game_over)
        Fond.delete(BT1)
        if T1.détruite!=True:
            fenetre.after(randint(500,1300), tirerT1)

#fonction de tire de la tourelle2
def tirerT2():
    global T2
    global Tank
    global BT2
    global BalleT2
    if T2.x<Tank.x:
        T2.direct="D"
        Fond.itemconfig(T2I, image=Fichier[17])
    elif T2.x>Tank.x:
        T2.direct="G"
        Fond.itemconfig(T2I, image=Fichier[16])
    elif T2.y>Tank.y:
        T2.direct="H"
        Fond.itemconfig(T2I, image=Fichier[18])
    elif T2.y<Tank.y:
        T2.direct="B"
        Fond.itemconfig(T2I, image=Fichier[19])
    BalleT2=balle(T2.x,T2.y,T2.attaquer(),T2.direct)
    if BalleT2.direct=="H":
        BT2=Fond.create_image(BalleT2.x+7, BalleT2.y+7, image=Fichier[-9], anchor='nw')
    if BalleT2.direct=="B":
        BT2=Fond.create_image(BalleT2.x+7, BalleT2.y+7, image=Fichier[-8], anchor='nw')
    if BalleT2.direct=="G":
        BT2=Fond.create_image(BalleT2.x+7, BalleT2.y+7, image=Fichier[-11], anchor='nw')
    if BalleT2.direct=="D":
        BT2=Fond.create_image(BalleT2.x+7, BalleT2.y+7, image=Fichier[-10], anchor='nw')

    rec_tirerT2()

def rec_tirerT2():
    global BT2
    global BalleT2
    global Tank
    if not (BalleT2.x,BalleT2.y)in Mure and (BalleT2.x,BalleT2.y)!=(Tank.x,Tank.y):
        if BalleT2.direct=="B":
                BalleT2.Desendre(18)
        if BalleT2.direct=="H":
                BalleT2.Monte(18)
        if BalleT2.direct=="D":
                BalleT2.Droite(18)
        if BalleT2.direct=="G":
                BalleT2.Gauche(18)
        Fond.coords(BT2,BalleT2.x+7, BalleT2.y+7)
        fenetre.after(20,rec_tirerT2)
    else:
        if (BalleT2.x,BalleT2.y)==(Tank.x,Tank.y):
            vie1=Tank.nbvie
            Tank.subir_degats(BalleT2.dégat)
            Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
            if vie1!=Tank.nbvie:
                anim_mort()
                if Tank.détruite:
                    fenetre.after(600,game_over)
        Fond.delete(BT2)
        if T2.détruite!=True:
            fenetre.after(randint(500,1300), tirerT2)

#fonction de tire de la tourelle3
def tirerT3():
    global T3
    global Tank
    global BT3
    global BalleT3
    if T3.x<Tank.x:
        T3.direct="D"
        Fond.itemconfig(T3I, image=Fichier[17])
    elif T3.x>Tank.x:
        T3.direct="G"
        Fond.itemconfig(T3I, image=Fichier[16])
    elif T3.y>Tank.y:
        T3.direct="H"
        Fond.itemconfig(T3I, image=Fichier[18])
    elif T3.y<Tank.y:
        T3.direct="B"
        Fond.itemconfig(T3I, image=Fichier[19])
    BalleT3=balle(T3.x,T3.y,T3.attaquer(),T3.direct)
    if BalleT3.direct=="H":
        BT3=Fond.create_image(BalleT3.x+7, BalleT3.y+7, image=Fichier[-9], anchor='nw')
    if BalleT3.direct=="B":
        BT3=Fond.create_image(BalleT3.x+7, BalleT3.y+7, image=Fichier[-8], anchor='nw')
    if BalleT3.direct=="G":
        BT3=Fond.create_image(BalleT3.x+7, BalleT3.y+7, image=Fichier[-11], anchor='nw')
    if BalleT3.direct=="D":
        BT3=Fond.create_image(BalleT3.x+7, BalleT3.y+7, image=Fichier[-10], anchor='nw')

    rec_tirerT3()

def rec_tirerT3():
    global BT3
    global BalleT3
    global Tank
    if not (BalleT3.x,BalleT3.y)in Mure and (BalleT3.x,BalleT3.y)!=(Tank.x,Tank.y):
        if BalleT3.direct=="B":
                BalleT3.Desendre(18)
        if BalleT3.direct=="H":
                BalleT3.Monte(18)
        if BalleT3.direct=="D":
                BalleT3.Droite(18)
        if BalleT3.direct=="G":
                BalleT3.Gauche(18)
        Fond.coords(BT3,BalleT3.x+7, BalleT3.y+7)
        fenetre.after(20,rec_tirerT3)
    else:
        if (BalleT3.x,BalleT3.y)==(Tank.x,Tank.y):
            vie1=Tank.nbvie
            Tank.subir_degats(BalleT3.dégat)
            Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
            if vie1!=Tank.nbvie:
                anim_mort()
                if Tank.détruite:
                    fenetre.after(600,game_over)
        Fond.delete(BT3)
        if T3.détruite!=True:
            fenetre.after(randint(500,1300), tirerT3)
#fonction de tire de la tourelle3
def tirerT4():
    global T4
    global Tank
    global BT4
    global BalleT4
    if T4.x<Tank.x:
        T4.direct="D"
        Fond.itemconfig(T4I, image=Fichier[17])
    elif T4.x>Tank.x:
        T4.direct="G"
        Fond.itemconfig(T4I, image=Fichier[16])
    elif T4.y>Tank.y:
        T4.direct="H"
        Fond.itemconfig(T4I, image=Fichier[18])
    elif T4.y<Tank.y:
        T4.direct="B"
        Fond.itemconfig(T4I, image=Fichier[19])
    BalleT4=balle(T4.x,T4.y,T4.attaquer(),T4.direct)
    if BalleT4.direct=="H":
        BT4=Fond.create_image(BalleT4.x+7, BalleT4.y+7, image=Fichier[-9], anchor='nw')
    if BalleT4.direct=="B":
        BT4=Fond.create_image(BalleT4.x+7, BalleT4.y+7, image=Fichier[-8], anchor='nw')
    if BalleT4.direct=="G":
        BT4=Fond.create_image(BalleT4.x+7, BalleT4.y+7, image=Fichier[-11], anchor='nw')
    if BalleT4.direct=="D":
        BT4=Fond.create_image(BalleT4.x+7, BalleT4.y+7, image=Fichier[-10], anchor='nw')
    rec_tirerT4()
def rec_tirerT4():
    global BT4
    global BalleT4
    global Tank
    if not (BalleT4.x,BalleT4.y)in Mure and (BalleT4.x,BalleT4.y)!=(Tank.x,Tank.y):
        if BalleT4.direct=="B":
                BalleT4.Desendre(18)
        if BalleT4.direct=="H":
                BalleT4.Monte(18)
        if BalleT4.direct=="D":
                BalleT4.Droite(18)
        if BalleT4.direct=="G":
                BalleT4.Gauche(18)
        Fond.coords(BT4,BalleT4.x+7, BalleT4.y+7)
        fenetre.after(20,rec_tirerT4)
    else:
        if (BalleT4.x,BalleT4.y)==(Tank.x,Tank.y):
            vie1=Tank.nbvie
            Tank.subir_degats(BalleT4.dégat)
            Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
            if vie1!=Tank.nbvie:
                anim_mort()
                if Tank.détruite:
                    fenetre.after(600,game_over)
        Fond.delete(BT4)
        if T4.détruite!=True:
            fenetre.after(randint(500,1300), tirerT4)
#fonction de tire de la tourelle5
def tirerT5():
    global T5
    global Tank
    global BT5
    global BalleT5
    if T5.x<Tank.x:
        T5.direct="D"
        Fond.itemconfig(T5I, image=Fichier[17])
    elif T5.x>Tank.x:
        T5.direct="G"
        Fond.itemconfig(T5I, image=Fichier[16])
    elif T5.y>Tank.y:
        T5.direct="H"
        Fond.itemconfig(T5I, image=Fichier[18])
    elif T5.y<Tank.y:
        T5.direct="B"
        Fond.itemconfig(T5I, image=Fichier[19])
    BalleT5=balle(T5.x,T5.y,T5.attaquer(),T5.direct)
    if BalleT5.direct=="H":
        BT5=Fond.create_image(BalleT5.x+7, BalleT5.y+7, image=Fichier[-9], anchor='nw')
    if BalleT5.direct=="B":
        BT5=Fond.create_image(BalleT5.x+7, BalleT5.y+7, image=Fichier[-8], anchor='nw')
    if BalleT5.direct=="G":
        BT5=Fond.create_image(BalleT5.x+7, BalleT5.y+7, image=Fichier[-11], anchor='nw')
    if BalleT5.direct=="D":
        BT5=Fond.create_image(BalleT5.x+7, BalleT5.y+7, image=Fichier[-10], anchor='nw')
    rec_tirerT5()
def rec_tirerT5():
    global BT5
    global BalleT5
    global Tank
    if not (BalleT5.x,BalleT5.y)in Mure and (BalleT5.x,BalleT5.y)!=(Tank.x,Tank.y):
        if BalleT5.direct=="B":
                BalleT5.Desendre(18)
        if BalleT5.direct=="H":
                BalleT5.Monte(18)
        if BalleT5.direct=="D":
                BalleT5.Droite(18)
        if BalleT5.direct=="G":
                BalleT5.Gauche(18)
        Fond.coords(BT5,BalleT5.x+7, BalleT5.y+7)
        fenetre.after(20,rec_tirerT5)
    else:
        if (BalleT5.x,BalleT5.y)==(Tank.x,Tank.y):
            vie1=Tank.nbvie
            Tank.subir_degats(BalleT5.dégat)
            Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
            if vie1!=Tank.nbvie:
                anim_mort()
                if Tank.détruite:
                    fenetre.after(600,game_over)
        Fond.delete(BT5)
        if T5.détruite!=True:
            fenetre.after(randint(500,1300), tirerT5)
#fonction de tire de la tourelle6
def tirerT6():
    global T6
    global Tank
    global BT6
    global BalleT6
    if T6.x<Tank.x:
        T6.direct="D"
        Fond.itemconfig(T6I, image=Fichier[17])
    elif T6.x>Tank.x:
        T6.direct="G"
        Fond.itemconfig(T6I, image=Fichier[16])
    elif T6.y>Tank.y:
        T6.direct="H"
        Fond.itemconfig(T6I, image=Fichier[18])
    elif T6.y<Tank.y:
        T6.direct="B"
        Fond.itemconfig(T6I, image=Fichier[19])
    BalleT6=balle(T6.x,T6.y,T6.attaquer(),T6.direct)
    if BalleT6.direct=="H":
        BT6=Fond.create_image(BalleT6.x+7, BalleT6.y+7, image=Fichier[-9], anchor='nw')
    if BalleT6.direct=="B":
        BT6=Fond.create_image(BalleT6.x+7, BalleT6.y+7, image=Fichier[-8], anchor='nw')
    if BalleT6.direct=="G":
        BT6=Fond.create_image(BalleT6.x+7, BalleT6.y+7, image=Fichier[-11], anchor='nw')
    if BalleT6.direct=="D":
        BT6=Fond.create_image(BalleT6.x+7, BalleT6.y+7, image=Fichier[-10], anchor='nw')

    rec_tirerT6()
def rec_tirerT6():
    global BT6
    global BalleT6
    global Tank
    if not (BalleT6.x,BalleT6.y)in Mure and (BalleT6.x,BalleT6.y)!=(Tank.x,Tank.y):
        if BalleT6.direct=="B":
                BalleT6.Desendre(18)
        if BalleT6.direct=="H":
                BalleT6.Monte(18)
        if BalleT6.direct=="D":
                BalleT6.Droite(18)
        if BalleT6.direct=="G":
                BalleT6.Gauche(18)
        Fond.coords(BT6,BalleT6.x+7, BalleT6.y+7)
        fenetre.after(20,rec_tirerT6)
    else:
        if (BalleT6.x,BalleT6.y)==(Tank.x,Tank.y):
            vie1=Tank.nbvie
            Tank.subir_degats(BalleT6.dégat)
            Pv.configure(text='Pv:'+str(Tank.pv)+'/'+str(Tank.pvmax))
            if vie1!=Tank.nbvie:
                anim_mort()
                if Tank.détruite:
                    fenetre.after(600,game_over)
        Fond.delete(BT6)
        if T6.détruite!=True:
            fenetre.after(randint(500,1300), tirerT6)
#--------------------------------------------------------------------
#Fonctionn pour afficher la carte
def affiche_cart(data,Fichier):
    global QGcoords
    for y in range(20):
        for x in range(20):
            if data[y][x]=='|':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[0], anchor='nw')
                Mure.append((x*18,y*18))
            elif data[y][x]=='-':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[1], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='D':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[2], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='B':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[3], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='H':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[4], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='G':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[5], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='C':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[6], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='=':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[7], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='+':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[8], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='!':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[9], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='.':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[10], anchor='nw')
                Mure.append((x*18, y*18))
            elif data[y][x]=='V':
                Viecoord.append((x*18, y*18))
            elif data[y][x]=='#':
                indice=randint(1,100)
                if indice>=1  and indice<1:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-2], anchor='nw')
                elif indice<50:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-1], anchor='nw')
                else:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-3], anchor='nw')

                Tcoords.append((x*18,y*18))
            elif data[y][x]=='X':
                indice=randint(1,100)
                if indice>=1  and indice<1:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-2], anchor='nw')
                elif indice<50:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-1], anchor='nw')
                else:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-3], anchor='nw')
                QGcoords=(x*18,y*18)
            elif data[y][x]=='R':
                Matt = Fond.create_image(x*18, y*18, image=Fichier[-5], anchor='nw')
                Bcoorgs.append((x*18, y*18))
            else:
                indice=randint(1,100)
                if indice>=1  and indice<1:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-2], anchor='nw')
                elif indice<50:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-1], anchor='nw')
                else:
                    Matt = Fond.create_image(x*18, y*18, image=Fichier[-3], anchor='nw')
#--------------------------------------------------------------------















# Création de la fenetre de jeux
fenetre = Tk()
fenetre.title("Tank Wars")
#initialisation des variable:
Tank=tank(18,18,10,4,25)
niv=1
cd=0
cdD=0
Tdétruite=0
QGdétruite=0
score=0
Fichier=charge_fichier()
F=[]
direcrt="H"
tir=False
#création et afichage du menue
Home=Canvas(fenetre,width=360, height=360, bg="Red")
Quit=Button(Home, width=6, height=1, text="Quiter X", command = destro)
Quit.place(x = 365, y = 0, anchor = "ne")
Home.pack()
F.append(PhotoImage(file="écran_titre.png"))
M = Home.create_image(2, 2, image=F[0], anchor='nw')
Play=Button(Home, width=12, height=2, text="PLAY |>", command = PdM)
Play.place(x = 60, y = 250, anchor = "nw")
fenetre.mainloop()