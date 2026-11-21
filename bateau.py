class Bateau:
    marque = "B"
    nom = "Bateau"
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        coords = []
        for i in range(self.longueur):
            if self.vertical:
                coords.append((self.ligne + i, self.colonne))
            else:
                coords.append((self.ligne, self.colonne + i))
        return coords

    def chevauche(self, autre_bateau):
        pos_self = self.positions()
        pos_autre = autre_bateau.positions()
        for pos in pos_self:
            if pos in pos_autre:
                return True
        return False

    def est_coule(self, grille):
        for ligne, colonne in self.positions():
            if not grille.est_dans_grille(ligne, colonne):
                return False
            idx = grille._indice(ligne, colonne)
            if grille.matrice[idx] != "x":
                return False
        return True

class PorteAvion(Bateau):
    marque = "P"
    nom = "Porte-avion"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)

class Croiseur(Bateau):
    marque = "C"
    nom = "Croiseur"
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)

class Torpilleur(Bateau):
    marque = "T"
    nom = "Torpilleur"
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)


class SousMarin(Bateau):
    marque = "S"
    nom = "Sous-marin"
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)