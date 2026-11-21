from grille import Grille
g = Grille(5, 8)
while True:
    print(g)
    x = int(input("Ligne (x) : "))
    y = int(input("Colonne (y) : "))
    g.tirer(x, y)