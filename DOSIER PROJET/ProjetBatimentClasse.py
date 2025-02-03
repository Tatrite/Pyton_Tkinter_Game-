# Créé par flofu, le 08/11/2022 en Python 3.7
class Unite:
    def __init__(self,x,y,pv,cp,ap):
        assert type(x)==int and x>=0
        assert type(y)==int and y>=0
        assert type(pv)==int and pv>0
        assert type(cp)==int and cp>=0
        assert type(ap)==int and ap>=0
        #Constructeur de La class Unite
        self.x=x
        self.y=y
        self.pv=pv
        self.cp=cp
        self.ap=ap
        self.direct="G"
        self.détruite=False

    def GetPv(self):
        #accesseur en lécture des Pv actuel de l'unité
        return self.pv

    def attaquer(self):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        return self.cp

    def subir_degats(self,degats):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        assert type(degats) == int and degats>=0
        npv= self.pv-degats
        if npv > 0:
            self.pv=npv
        else:
            self.pv=0
            self.détruit()


    def détruit(self):
        self.détruite=True


class QG:
    def __init__(self,x,y,pv):
        assert type(x)==int and x>=0
        assert type(y)==int and y>=0
        assert type(pv)==int and pv>0
        #Constructeur de La class Unite
        self.x=x
        self.y=y
        self.pv=pv
        self.détruite=False

    def GetPv(self):
        #accesseur en lécture des Pv actuel de l'unité
        return self.pv


    def subir_degats(self,degats):
        #Déscription:
        #Paramétres:
        #Précondition:
        #Postcondition:
        assert type(degats) == int and degats>=0
        npv= self.pv-(degats)
        npv= round(npv)
        if npv >= 0:
            self.pv=npv
        else:
            self.pv=0
            self.détruit()


    def détruit(self):
        self.détruite=True


