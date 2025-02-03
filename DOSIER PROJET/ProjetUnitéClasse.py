# Créé par flofu, le 28/09/2022 en Python 3.7
from math import sqrt
class tank:
    def __init__(self,x,y,pv,cp,ap):
        assert type(x)==int and x>=0
        assert type(y)==int and y>=0
        assert type(pv)==int and pv>0
        assert type(cp)==int and cp>=0
        assert type(ap)==int and ap>=0
        #Constructeur de La class Unite
        self.x=x
        self.y=y
        self.pvmax=pv
        self.pv=pv
        self.cp=cp
        self.cpboost=0
        self.ap=ap
        self.apboost=0
        self.nbvie=3
        self.mode="facile"
        self.détruite=False
        self.direct='D'

    def GetX(self):
        #accesseur en lécture de l'ablisse de l'unité
        return self.x
    def GetY(self):
        #accesseur en lécture de l'Ordoné de l'unité
        return self.y
    def GetPvmax(self):
        #accesseur en lécture des Pv Maximale de l'unité
        return self.pvmax
    def GetPv(self):
        #accesseur en lécture des Pv actuel de l'unité
        return self.pv
    def GetCp(self):
        #accesseur en lécture des Point d'ataque de l'unité
        return self.cp
    def GetGold(self):
        #accesseur en lécture de la quantité de piéce d'or de l'unité
        return self.gold

    def GetNbvie(self):
        #accécseur en lécture du noubre de vie réstante
        return self.nbvie

    def calc_dist(self,bat):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        return sqrt((self.x-bat.x)+(self.y-bat.y))

    def finir_niv(self,niv):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        if mode=="facile":
            self.pv+=self.pvmax

    def augmenter_ap(self,ap):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        self.ap+=ap

    def augmenter_cp(self,cp):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        self.cp+=cp

    def augmenter_pv(self,pv):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        self.pvmax+=pv
        if self.mode=="facile":
            self.pv=self.pvmax

    def attaquer(self):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        return self.cp+self.cpboost

    def deplacer(self,dx,dy):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        self.x+=dx
        self.y+=dy

    def aficher_statistique(self):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        return (self.x,self.y,self.pvmax,self.pv,self.cp,self.ap,self.gold)

    def augmenter_po(self,po_gagnees):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        assert type(po_gagnees) == int
        self.gold+=po_gagnees

    def subir_degats(self,degats):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        assert type(degats) == int and degats>=0
        npv= self.pv-(degats-(degats*(self.ap/(self.ap+100))))
        npv= round(npv)
        if npv >= 0:
            self.pv=npv
        else:
            self.pv=0
            self.détruit()

    def reparer(self,Pv_gagnes):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        assert type(Pv_gagnes) == int and Pv_gagnes>=0 and self.pv!=0
        npv= self.pv+Pv_gagnes
        if npv >= self.pvmax:
            self.pv=self.pvmax
        else:
            self.pv=npv


    def boost(self,boostap,boostcp):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        self.cpboost=boostcp
        self.apboost=boostap


    def détruit(self):
        self.nbvie-=1
        if  self.nbvie<=0:
            self.détruite=True

        self.pv=self.pvmax

