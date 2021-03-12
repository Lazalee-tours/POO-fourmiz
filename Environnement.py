# à mettre dans la classe Environnement
class Environement :
    def __init__(self, largeur=1, hauteur=1, nbsucre=0):
        self.terrain=[]
        self.nbsucre=0
        self.origine = Case()
        
        for y in range (hauteur):
            ligne=[]
            for x in range(largeur):
                macase = Case(x=x, y=y)
                if len(ligne)>0 :
                    ligne[-1].voisine_droite(macase)
                if len(self.terrain)>0:
                    self.terrain[-1][x].voisine_haut(macase)
                ligne.append(macase)
                
            self.terrain.append(ligne)
        
    def tour_suivant(self):
        #for macase in range(terrain) :
            #terrain.tour_suivant() ?
            #tour_suivant(terrain)  ?
        for y in range (hauteur):
            ligne=[]
            for x in range(largeur):
                macase = Case(x=x, y=y)
                if len(ligne)>0 :
                    ligne[-1].tour_suivant(macase)
                if len(self.terrain)>0:
                    self.terrain[-1][x].tour_suivant(macase)           
            
    def afficher(self):
        # Initialisation des listes des coordonnées des murs
        Xmurs = []
        Ymurs = []

        # Initialisation des listes des coordonnées des morceaux de sucres
        Xsucres = []
        Ysucres = []

        # Initialisation des quantités de pheromones
        pheromones = np.zeros((len(self.terrain[0]),len(self.terrain)))

        for ligne in self.terrain: # Pour chaque ligne du terrain
            for case in ligne: # Pour chaque case de la ligne
                # Ajout des coordonnées de la case dans les listes appropriées
                if (case.statut == "Mur"): # Si la case contient un mur
                    Xmurs.append(case.x) 
                    Ymurs.append(case.y)
                elif (case.statut == "Sucre"): # Si la case contient un morceau de sucre
                    Xsucres.append(case.x)
                    Ysucres.append(case.y)
                # Attribuer la quantité de pheromone de la case
                pheromones[case.y][case.x] = case.pheromone 
        # Tracer les murs
        plt.scatter(Xmurs,Ymurs,s=5,color ="black", marker = "s")
        # Dessiner les morceaux de sucres
        plt.scatter(Xsucres,Ysucres,s=5,color ="gray", marker = "8")
        # Représenter les traces de pheromones
        plt.imshow(pheromones, interpolation="nearest", cmap="Blues", origin="lower")