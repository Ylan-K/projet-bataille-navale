from bateau import Bateau
b1 = Bateau(2, 2, longueur=3, vertical=False)
b2 = Bateau(1, 3, longueur=3, vertical=True)
print("Chevauchement (b1, b2) :", b1.chevauche(b2))

b3 = Bateau(2, 2, longueur=3, vertical=False)
b4 = Bateau(4, 0, longueur=2, vertical=False)
print("Chevauchement (b3, b4) :", b3.chevauche(b4))