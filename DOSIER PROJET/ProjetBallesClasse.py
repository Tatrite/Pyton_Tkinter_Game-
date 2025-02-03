# Créé par flofu, le 28/11/2022 en Python 3.7
class balle:
    def __init__(self,x,y,dégat,direct):
        self.x=x
        self.y=y
        self.dégat=dégat
        self.direct= direct

    def Monte(self,dist):
        self.y-=dist

    def Desendre(self,dist):
        self.y+=dist

    def Gauche(self,dist):
        self.x-=dist

    def Droite(self,dist):
        self.x+=dist