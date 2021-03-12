from random import randint
class Fourmi :
    def __init__(self, origine, positionDépart): #mode="exploratrice"
        self.coord = positionDépart #déf la coordonnée de la fourmi comme la position de départ
        self.pathdone = [self.coord] #chemin fait par la fourmi = mémoire
        self.origine = origine #l'origine de la fourmi est défi comme l'origine
        #self.mode = mode  définir la classe fourmi de base avant de mettre ce mode
        self.maison = False #retour à la maison pas possible dès le départ
        self.direction = randint(0,3) #la direction est random entre les 4 possibilités
        self.lastCoord = None #initialisation de la dernière coordonnée à 0
        

    def mouvement(self):
        if self.origine.gsucres[self.coord[0][self.coord[1]]: #si sur le chemin au départ de l'origine, la fourmi a trouvé du sucre (self.coord[1] = 1 sucre) gsucres = grille de sucres
            self.maison = True #retour maison
            shorten(self.pathdone) #sans boucle
            if self.maison: #si pour le retour à la maison
                if self.pathdone: #si il reste du chemin
                    self.lastCoord = self.coord #sa dernière coordonnée devient sa coordonnée
                    self.coord = self.pathdone.pop() #les coordonnées de la fourmi récupèrent le chemin fait par la fourmi (pop retourne les objets d'une liste)
                else:
                    self.maison = False #la fourmi repart
            else: #pas trouvé de nourriture
                directions = [(-1, 0), #donne toutes les directions possibles par la fourmi (ici, en haut, en bas, à gauche et à droite, déf dans la classe case)
                            (0, -1), (0, 1),
                            (1, 0)]
                asucre = self.origine.gsucres #elle doit chercher du sucre 
                sucre=[(asucre[(self.coord[0] + x) % self.origine.xmax] #le mouvement init + x est divisé par le xmax de l'origine du mouvement
                                [(self.coord[1] + y) % self.origine.ymax], 
                                [(self.coord[0] + x) % self.origine.xmax,
                                (self.coord[1]) + y) % self.origine.ymax])
                        for (x, y) in directions] #pour chaque direction, on "scanne" x et y afin d'y chercher du sucre
                sucre.sort() #trie la liste qui en découle 
                if (sucre[-1][0]): #si du sucre est trouvé à côté
                    self.lastCoord = self.coord #la fourmi y va
                    self.coord = sucre[-1][1] #le mouvement se fait vers le sucre
                else:
                    terrain = self.origine.pheromones #recherche des phéromones
                    pheromone = [(terrain[(self.coord[0] + x) % self.origine.xmax]
                                        [(self.coord[1] + y) % self.origine.ymax],
                                        [(self.coord[0] + x) % self.origine.xmax,
                                        (self.coord[1] + y) % self.origine.ymax])
                                for (x,y) in directions] #on scanne cette fois-ci le terrain pour y trouver des phéromones
                    actuelPheromones = [(i, j) for (i, j) in pheromone if (i!=0)] #
                    lenPhero = len(actuelPheromones) #lenPhero prend pour valeur la taille de actuelPheromones
                    if lenPhero > 0: #si lenPhero est supérieur à 0 alors = phéromones à côté
                        if (randint(0, 100) < 95): #à 95% on suit la plus forte présence de phéromones
                            nouvelleCoord = actuelPheromones[randint(0, lenPhero-1)][1]  
                        else:
                            nouvelleCoord = pheromone[randint(0, 3)][1] #sinon la fourmi continue de chercher
                    else: #pas de phéromones à côté
                        nouvelleCoord =pheromone[randit(0,3)][1]
                    while nouvelleCoord == self.lastCoord: #tant qu'on ne revient pas sur nos pas
                        nouvelleCoord = pheromone[randint(0,3)][1]
                    self.lastCoord = self.coord
                    self.coord = nouvelle.coord
                    self.pathdone += [self.coord[:]]