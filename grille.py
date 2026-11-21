from termcolor import colored
class Grille:
    VIDE = "~"
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.matrice = [self.VIDE] * (nombre_lignes * nombre_colonnes)

    def _indice(self, ligne, colonne):
        return ligne * self.nombre_colonnes + colonne

    def est_dans_grille(self, ligne, colonne):
        return (
            0 <= ligne < self.nombre_lignes
            and 0 <= colonne < self.nombre_colonnes
        )

    def tirer(self, ligne, colonne, touche="x"):
        if self.est_dans_grille(ligne, colonne):
            idx = self._indice(ligne, colonne)
            self.matrice[idx] = touche

    def ajoute(self, bateau):
        positions = bateau.positions()
        for ligne, colonne in positions:
            if not self.est_dans_grille(ligne, colonne):
                return False

        for ligne, colonne in positions:
            idx = self._indice(ligne, colonne)
            self.matrice[idx] = bateau.marque
        return True

    def __str__(self):
        lignes_texte = []
        for l in range(self.nombre_lignes):
            debut = l * self.nombre_colonnes
            fin = debut + self.nombre_colonnes
            cases = []
            for c in self.matrice[debut:fin]:
                if c == "~":
                    cases.append(colored(c, "blue"))
                elif c == "x":
                    cases.append(colored(c, "red"))
                else:
                    cases.append(colored(c, "green"))
            lignes_texte.append(" ".join(cases))
        return "\n".join(lignes_texte)