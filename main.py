import random
from bateau import Croiseur, PorteAvion, SousMarin, Torpilleur
from grille import Grille
from termcolor import colored
def placer_bateaux_aleatoirement(grille, bateaux):
    bateaux_places = []
    for bateau_classe in bateaux:
        possibilites = []
        for l in range(grille.nombre_lignes):
            for c in range(grille.nombre_colonnes):
                for vertical in [False, True]:
                    candidat = bateau_classe(l, c, vertical=vertical)
                    dans_grille = True
                    for pl, pc in candidat.positions():
                        if not grille.est_dans_grille(pl, pc):
                            dans_grille = False
                            break
                    if not dans_grille:
                        continue
                    collision = False
                    for deja_place in bateaux_places:
                        if candidat.chevauche(deja_place):
                            collision = True
                            break

                    if not collision:
                        possibilites.append(candidat)

        if len(possibilites) > 0:
            choisi = random.choice(possibilites)
            bateaux_places.append(choisi)
    return bateaux_places

def main():
    grille = Grille(8, 10)
    classes_bateaux = [PorteAvion, Croiseur, Torpilleur, SousMarin]
    bateaux = placer_bateaux_aleatoirement(grille, classes_bateaux)
    bateaux_coules = []
    coups = 0
    while len(bateaux_coules) < len(bateaux):
        print()
        print(grille)
        ligne = int(input(colored("Ligne : ","yellow")))
        colonne = int(input(colored("Colonne : ","yellow")))
        coups = coups + 1
        touche_un_bateau = False
        for b in bateaux:
            if (ligne, colonne) in b.positions():
                touche_un_bateau = True
                grille.tirer(ligne, colonne, touche="x")
                print(colored("Touché !","green"))
                if b not in bateaux_coules and b.est_coule(grille):
                    bateaux_coules.append(b)
                    grille.ajoute(b)
                    print(colored("Coulé ! Vous avez coulé le", "red"), b.nom)
                break

        if not touche_un_bateau:
            grille.tirer(ligne, colonne, touche="x")
            print(colored("Dans l'eau !","blue"))
    print()
    print(grille)
    print(colored("Bravo, tous les bateaux sont coulés en", "green"), coups, colored("coups !","green"))

if __name__ == "__main__":
    main()