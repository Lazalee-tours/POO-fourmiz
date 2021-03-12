import math
class Case:
    def __init__(self,x=0,y=0,statut= "route"):
        self.haut = None
        self.bas = None
        self.gauche = None
        self.droite = None
        self.x = x
        self.y = y
        self.pheromones= 0
        self.statut=statut #valeur par default en "route"
        
    def tour_suivant(self): #fonction pr enlever 5% des pheromones des cases
        self.pheromones = 0.95*self.pheromones
        
    def distance(self, autre): #calcul entre 2 points x et y en ligne droite
        dist=(self.x-autre.x)**2+(self.y-autre.y)**2
        return math.sqrt(dist)
        
    def voisine_haut (self, voisine):
        self.haut = voisine
        voisine.bas = self
        voisine.x = self.x
        voisine.y = self.y+1
    
    def voisine_bas (self, voisine):
        self.bas = voisine
        voisine.haut = self
        voisine.x = self.x
        voisine.y = self.y - 1
        
    def voisine_droite (self, voisine):
        self.droite = voisine
        voisine.gauche = self
        voisine.x = self.x+1
        voisine.y = self.y
        
    def voisine_gauche (self, voisine):
        self.droite = voisine
        voisine.gauche = self
        voisine.x = self.x - 1
        voisine.y = self.y