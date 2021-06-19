import turtle
from random import randint
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO, ORIGINtBxB,
    ORIGINtByB, DIAMETREGOBI, ORIGINtBxJ, ORIGINtByJ
)

###############################################################################
"""Ce fichier contient les fonctions pour dessiner la table et les gobies"""
###############################################################################

def dessin_Cercle(x, y, color):
    """
    Fonction qui dessine un cercle plein de rayon égal à celle des gobies avec
    application de ECHELLE. On entre les coordonnées (en turtle centré) et la
    couleurs.

    La fonction turtle.circle() prend le rayon du cerlce en paramètre.
    Le cercle est déssiné en partant de la position de la turtle en considérant
    qu'elle se trouve au point le plus bas du cercle (en bas du rayon parallèle
    à l'axe des ordonnées).

    Si on veut tracer un cercle dont le centre est les coordonnées x;y des
    paramètres il faut appliquer un déplactment de longeur un rayon vers le
    bas.
    """
    turtle.penup()
    turtle.goto(x, y-(DIAMETREGOBI/2)*ECHELLE)
    turtle.pen(pencolor=color, fillcolor=color)
    turtle.begin_fill()
    turtle.circle((DIAMETREGOBI/2)*ECHELLE)
    turtle.end_fill()


def dessin_Zone_Couleur(x, y, long, large, color):
    # long : longeur sur l'axe des x en CTC
    # large : largeur sur l'axe des y en CTC
    """
    Dessine un rectangle plein de couleur : color, et de dimensions long*large.
    Les coordonnées en x;y en entré sont celle de la base inférieur gauche
    du rectangle sur le dessin.
    """
    turtle.goto(x, y)
    turtle.pen(pencolor=color, fillcolor=color)
    turtle.begin_fill()
    turtle.forward(long)
    turtle.left(90)
    turtle.forward(large)
    turtle.left(90)
    turtle.forward(long)
    turtle.left(90)
    turtle.forward(large)
    turtle.left(90)
    turtle.end_fill()

def dessin_Zone(x, y, long, large, color):
    # long : longeur sur l'axe des x en CTC
    # large : largeur sur l'axe des y en CTC
    """
    Dessine un rectangle vide de couleur : color, et de dimensions long*large.
    Les coordonnées en x;y en entré sont celle de la base inférieur gauche
    du rectangle sur le dessin.
    """
    turtle.goto(x, y)
    turtle.pen(pencolor=color)
    turtle.pendown()
    turtle.forward(long)
    turtle.left(90)
    turtle.forward(large)
    turtle.left(90)
    turtle.forward(long)
    turtle.left(90)
    turtle.forward(large)
    turtle.left(90)
    turtle.penup()
    turtle.pen(pencolor="black")

###############################################################################

def dessin_Gobies_init():
    """
    Dessine l'ensemble des gobies de la table (à ne faire qu'une fois). Dans
    l'état les éléments de la liste sont en unité turtle centré donc on applique
    juste ECHELLE.
    """
    for i in range(0, 24):
        dessin_Cercle(
            convert_CMOtoCTC(LISTEGOBI[i][0], "x"),
            convert_CMOtoCTC(LISTEGOBI[i][1], "y"),
            LISTEGOBI[i][2]
        )

def drawboard():
    """
    Fonction à utiliser une seule fois pour dessiner l'ensemble de la table au
    début de de la simulation.
    """
    turtle.colormode(0xFF)  # Set les couleurs en version RGB 255
    # Règle la vitesse et la taille de la tortue de dessin
    # Par définition il exite un objet nommé "turtle" qui nous sert uniquement
    # au dessin sur la table
    turtle.speed(100)
    turtle.shapesize(0.1, 0.1, 0.1)
    turtle.penup()

    # coordonnées turtle centrée = CTC
    # coordonnées mm centrée = CMC
    # coordonnées mm offset = CMO

    # dessiner le cadre
    dessin_Zone_Couleur(convert_CMOtoCTC(0, "x"),
        convert_CMOtoCTC(2000, "y"), 3000*ECHELLE, 2000*ECHELLE, AQA
    )
    # dessiner la zone de jeu1
    dessin_Zone(convert_CMOtoCTC(0, "x"),
        convert_CMOtoCTC(1070, "y"), 400*ECHELLE, 540*ECHELLE, BLE
    )
    # dessiner la zone de jeu2
    dessin_Zone(convert_CMOtoCTC(2600, "x"),
        convert_CMOtoCTC(1070, "y"), 400*ECHELLE, 540*ECHELLE, YL
    )
    # dessiner la zone de jeu jaune bas
    dessin_Zone(convert_CMOtoCTC(1150,"x"),
        convert_CMOtoCTC(2000, "y"), 100*ECHELLE, 300*ECHELLE, YL
    )
    # dessiner la zone de jeu bleu bas
    dessin_Zone(convert_CMOtoCTC(1750,"x"),
        convert_CMOtoCTC(2000, "y"), 100*ECHELLE, 300*ECHELLE, BLE
    )
    # dessiner les rochers
    dessin_Zone(convert_CMOtoCTC(889,"x"),
        convert_CMOtoCTC(2000, "y"), 22*ECHELLE, 150*ECHELLE, BLC
    )
    dessin_Zone(convert_CMOtoCTC(2089,"x"),
        convert_CMOtoCTC(2000, "y"), 22*ECHELLE, 150*ECHELLE, BLC
    )
    dessin_Zone(convert_CMOtoCTC(1489,"x"),
        convert_CMOtoCTC(2000, "y"), 22*ECHELLE, 300*ECHELLE, BLC
    )

    # dessiner les zones de couleurs des bases
    dessin_Zone_Couleur(
        convert_CMOtoCTC(0,"x"),
        convert_CMOtoCTC(530, "y"), 400*ECHELLE, 30*ECHELLE, GR
    )
    dessin_Zone_Couleur(
        convert_CMOtoCTC(0,"x"),
        convert_CMOtoCTC(1100, "y"), 400*ECHELLE, 30*ECHELLE, RD
    )
    dessin_Zone_Couleur(
        convert_CMOtoCTC(2600, "x"),
        convert_CMOtoCTC(530, "y"), 400*ECHELLE, 30*ECHELLE, RD
    )
    dessin_Zone_Couleur(
        convert_CMOtoCTC(2600, "x"),
        convert_CMOtoCTC(1100, "y"), 400*ECHELLE, 30*ECHELLE, GR
    )

    # dessiner les zones de couleurs des bases rochers
    dessin_Zone_Couleur(
        convert_CMOtoCTC(1050, "x"),
        convert_CMOtoCTC(2000, "y"), 100*ECHELLE, 300*ECHELLE, GR
    )
    dessin_Zone_Couleur(
        convert_CMOtoCTC(1250, "x"),
        convert_CMOtoCTC(2000, "y"), 100*ECHELLE, 300*ECHELLE, RD
    )
    dessin_Zone_Couleur(
        convert_CMOtoCTC(1650, "x"),
        convert_CMOtoCTC(2000, "y"), 100*ECHELLE, 300*ECHELLE, GR
    )
    dessin_Zone_Couleur(
        convert_CMOtoCTC(1850, "x"),
        convert_CMOtoCTC(2000, "y"), 100*ECHELLE, 300*ECHELLE, RD
    )

    dessin_Zone(convert_CMOtoCTC(0, "x"),
        convert_CMOtoCTC(2000, "y"), 3000*ECHELLE, 2000*ECHELLE, BLC
    )
    dessin_Gobies_init()
    turtle.title("Simulation de la coupe")
    turtle.home()   # Retourne en 0;0 CTC

###############################################################################

if __name__ == '__main__':
    # dessin_Gobies_init()
    drawboard()
    turtle.mainloop()
