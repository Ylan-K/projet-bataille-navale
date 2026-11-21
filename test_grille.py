from bateau import Bateau
from grille import Grille
def test_init():
    g = Grille(5, 8)
    assert isinstance(g, Grille)
    assert g.nombre_lignes == 5
    assert g.nombre_colonnes == 8
    assert len(g.matrice) == 40
    assert g.matrice[0] == "~"

def test_tirer():
    g = Grille(5, 8)
    g.tirer(2, 3)
    assert g.matrice[2 * 8 + 3] == "x"
    g.tirer(1, 1, touche="*")
    assert g.matrice[1 * 8 + 1] == "*"

def test_str():
    g = Grille(2, 3)
    assert isinstance(str(g), str)
    g.tirer(1, 2)
    assert "x" in str(g)

def test_ajoute():
    g = Grille(2, 3)
    b_ok = Bateau(1, 0, longueur=2, vertical=False)
    assert g.ajoute(b_ok) is True
    assert g.matrice == ["~", "~", "~", "B", "B", "~"]
    
    g2 = Grille(2, 3)
    b_trop_grand = Bateau(1, 0, longueur=4, vertical=True)
    assert g2.ajoute(b_trop_grand) is False
    assert g2.matrice == ["~", "~", "~", "~", "~", "~"]