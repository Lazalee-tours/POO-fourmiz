# à mettre dans la classe Colonie

def afficher(self):
    # Initialisation des listes des coordonnées des fourmies
    Xfourmies = []
    Yfourmies = []
    
    for membre in self.membres: # Pour chaque fourmi membre
        # Ajout des coordonnées de la case dans les listes appropriées
        Xfourmies.append(membre.case.x)
        Yfourmies.append(membre.case.y)
        
    # Dessiner les fourmis
    plt.scatter(Xfourmies, Yfourmies, color = "red", s=5, marker="o")
    # Dessiner la colonie
    plt.scatter([self.case.x],[self.case.y],color="brown", s=20, marker="*")