# coordonnées turtle centrée = CTC
# coordonnées mm centrée = CMC
# coordonnées mm offset = CMO

###############################################################################


def convert_CMOtoCTC(val, axe):
    if (axe == "x"):
        if (val == 1500):
            return (0)
        elif (val == 0):
            return (-1500*ECHELLE)
        elif (val == 3000):
            return (1500*ECHELLE)
        else:
            if (val < 1500):
                return(-ECHELLE*(1500-val))
            else:
                return(ECHELLE*(val-1500))
    if (axe == "y"):
        if (val == 1000):
            return (0)
        elif (val == 0):
            return (200)
        elif (val == 2000):
            return (-200)
        else:
            if (val < 1000):
                return(ECHELLE*(1000-val))
            else:
                return(-ECHELLE*(val-1000))


def convert_CTCtoCMO(val, axe):
    if (axe == "x"):
        if (val == 0):
            return (1500)
        elif (val == -300):
            return (0)
        elif (val == 300):
            return (3000)
        else:
            if (val < 0):
                return((300-(-val))/ECHELLE)
            else:
                return(val/ECHELLE+1500)
    if (axe == "y"):
        if (val == 0):
            return (1000)
        elif (val == -200):
            return (2000)
        elif (val == 200):
            return (0)
        else:
            if (val > 0):
                return((200-val)/ECHELLE)
            else:
                return((-val)/ECHELLE+1000)


###############################################################################


GR = (0, 166, 0)                    # Vert
RD = (229, 0, 0)                    # Rouge
BLE = (0, 76, 229)                  # Bleu
YL = (255, 191, 0)                  # Jaune
BLC = (0, 0, 0)                     # Noir
AQA = (79, 205, 251)                # Aqua
BOTCOLOR = (196, 196, 196)          # Couleur du Robot
ECHELLE = 1/5                       # Echelle des longueurs réel/simulation
DIMTABLE = (3000, 2000)             # Les dimensions de la tables en x;y en CMO
OFFSETX = DIMTABLE[0]//2
OFFSETY = DIMTABLE[1]//2
LFT = "left"
RGH = "right"
# En mm, distance entre le centre du robot et le centre des pinces
ENTRAX = 117.95
# Angle entre le vecteur robot et les vecteurs pinces
VALEUR_ROTATION_P1P2 = 30.0
# Origine du robot en CMO
ORIGINtBx = 250  # En CMO
ORIGINtBy = 800  # En CMO
DIAMETREGOBI = 75  # En mm
LONGUER_ACCEPTATION_PINCES = 50  # En mm
###############################################################################

# La liste va de 0 à 23, avec 0 à 3 dans les sous toples
# La valeur des coordonnées est en CMO.
LISTEGOBI = [
    (300, 400, RD, "QB1"),
    (445, 515, GR, "QB2"),
    (445, 1085, RD, "QB3"),
    (300, 1200, GR, "QB4"),
    (2700, 400, GR, "QJ1"),
    (2555, 515, RD, "QJ2"),
    (2555, 1085, GR, "QJ3"),
    (2700, 1200, RD, "QJ4"),
    (670, 100, RD, "LB1"),
    (956, 400, GR, "LB2"),
    (1100, 800, RD, "LB3"),
    (1270, 1200, GR, "LB4"),
    (2330, 100, GR, "LJ1"),
    (2044, 400, RD, "LJ2"),
    (1900, 800, GR, "LJ3"),
    (1730, 1200, RD, "LJ4"),
    (1005, 1955, RD, "CB1"),
    (1065, 1655, GR, "CB2"),
    (1335, 1655, RD, "CB3"),
    (1395, 1955, GR, "CB4"),
    (1605, 1955, RD, "CJ1"),
    (1665, 1655, GR, "CJ2"),
    (1935, 1655, RD, "CJ3"),
    (1995, 1955, GR, "CJ4"),
]

# La liste va de 0 à 23, avec 0 à 3 dans les sous toples
# La valeur des coordonnées est en CMC.
LISTEGOBI2 = [
    (-1200, 600, RD, "QB1"),
    (-1055, 485, GR, "QB2"),
    (-1055, -85, RD, "QB3"),
    (-1200, -200, GR, "QB4"),
    (1200, 600, GR, "QJ1"),
    (1055, 485, RD, "QJ2"),
    (1055, -85, GR, "QJ3"),
    (1200, -200, RD, "QJ4"),
    (-830, 900, RD, "LB1"),
    (-544, 600, GR, "LB2"),
    (-400, 200, RD, "LB3"),
    (-230, -200, GR, "LB4"),
    (830, 900, GR, "LJ1"),
    (544, 600, RD, "LJ2"),
    (400, 200, GR, "LJ3"),
    (230, -200, RD, "LJ4"),
    (-495, -955, RD, "CB1"),
    (-435, -655, GR, "CB2"),
    (-165, -655, RD, "CB3"),
    (-105, -955, GR, "CB4"),
    (105, -955, RD, "CJ1"),
    (165, -655, GR, "CJ2"),
    (435, -655, RD, "CJ3"),
    (495, -955, GR, "CJ4"),
]

# La liste va de 0 à 23, avec 0 à 3 dans les sous toples
# La valeur des coordonnées est en CTC.
LISTEGOBI3 = [
    (-240, 120, RD, "QB1"),
    (-211, 97, GR, "QB2"),
    (-211, -17, RD, "QB3"),
    (-240, -40, GR, "QB4"),
    (240, 120, GR, "QJ1"),
    (211, 97, RD, "QJ2"),
    (211, -17, GR, "QJ3"),
    (240, -40, RD, "QJ4"),
    (-166, 180, RD, "LB1"),
    (-108.8, 120, GR, "LB2"),
    (-80, 40, RD, "LB3"),
    (-46, -40, GR, "LB4"),
    (166, 180, GR, "LJ1"),
    (108.8, 120, RD, "LJ2"),
    (80, 40, GR, "LJ3"),
    (46, -40, RD, "LJ4"),
    (-99, -191, RD, "CB1"),
    (-87, -131, GR, "CB2"),
    (-33, -131, RD, "CB3"),
    (-21, -191, GR, "CB4"),
    (21, -191, RD, "CJ1"),
    (33, -131, GR, "CJ2"),
    (87, -131, RD, "CJ3"),
    (99, -191, GR, "CJ4"),
]
