from bateau import Bateau, Croiseur, PorteAvion, SousMarin, Torpilleur
from grille import Grille
def test_init_defaut():
    b = Bateau(1, 2)
    assert b.ligne == 1
    assert b.colonne == 2
    assert b.longueur == 1
    assert b.vertical is False

def test_positions():
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [
        (2, 3),
        (3, 3),
        (4, 3),
    ]

def test_chevauche():
    b1 = Bateau(2, 2, longueur=3, vertical=False)
    b2 = Bateau(1, 3, longueur=3, vertical=True)
    b3 = Bateau(0, 0, longueur=2, vertical=False)
    assert b1.chevauche(b2) is True
    assert b1.chevauche(b3) is False

def test_est_coule():
    g = Grille(5, 5)
    b = Bateau(1, 1, longueur=2, vertical=False)
    g.tirer(1, 1)
    assert b.est_coule(g) is False
    g.tirer(1, 2)
    assert b.est_coule(g) is True

def test_types_bateaux():
    pa = PorteAvion(0, 0)
    cr = Croiseur(0, 0)
    to = Torpilleur(0, 0)
    sm = SousMarin(0, 0)
    assert pa.longueur == 4 and pa.marque == "P"
    assert cr.longueur == 3 and cr.marque == "C"
    assert to.longueur == 2 and to.marque == "T"
    assert sm.longueur == 2 and sm.marque == "S"