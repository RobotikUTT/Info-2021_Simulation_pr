import turtle
from random import randint
from constantes import (
    LISTEGOBI, LISTEGOBI2, GR, RD, AQA, BLE, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO
)


def dessin_Gobies_init():
    """
    Dessine l'ensemble des gobies de la table (à ne faire qu'une fois). Dans
    l'état les éléments de la liste sont en unité turtle centré donc on applique
    juste ECHELLE.
    """
    for i in range(0, 24):
        dessin_Cercle(
            LISTEGOBI[i][0]*ECHELLE, LISTEGOBI[i][1]*ECHELLE, LISTEGOBI[i][2]
        )


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
    turtle.goto(x, y-(75/2)*ECHELLE)
    turtle.pen(pencolor=color, fillcolor=color)
    turtle.begin_fill()
    turtle.circle((75/2)*ECHELLE)
    turtle.end_fill()


def dessin_Zone_Couleur(x, y, long, large, color):
    # long : longeur sur l'axe des x
    # large : largeur sur l'axe des y
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
    # long : longeur sur l'axe des x
    # large : largeur sur l'axe des y
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
    dessin_Zone_Couleur(-300, -200, 600, 400, AQA)  # CTC
    # dessiner la zone de jeu1
    dessin_Zone(-300, -14, 80, 108, BLE)    # CTC
    # dessiner la zone de jeu2
    dessin_Zone(220, -14, 80, 108, YL)  # CTC
    # dessiner la zone de jeu jaune bas
    dessin_Zone(-70, -200, 20, 60, YL)  # CTC
    # dessiner la zone de jeu bleu bas
    dessin_Zone(50, -200, 20, 60, BLE)  # CTC
    # dessiner les rochers
    dessin_Zone(-122.2, -200, 4.4, 30, BLC) # CTC
    dessin_Zone(117.8, -200, 4.4, 30, BLC)  # CTC
    dessin_Zone(-2.2, -200, 4.4, 60, BLC)   # CTC

    # dessiner les zones de couleurs des bases
    dessin_Zone_Couleur(
        -1500*ECHELLE, 470*ECHELLE, 400*ECHELLE, 30*ECHELLE, GR
    )   # CMC
    dessin_Zone_Couleur(
        -1500*ECHELLE, -100*ECHELLE, 400*ECHELLE, 30*ECHELLE, RD
    )   # CMC
    dessin_Zone_Couleur(
        1100*ECHELLE, 470*ECHELLE, 400*ECHELLE, 30*ECHELLE, RD
    )   # CMC
    dessin_Zone_Couleur(
        1100*ECHELLE, -100*ECHELLE, 400*ECHELLE, 30*ECHELLE, GR
    )   # CMC
    # dessiner les zones de couleurs des bases rochers
    dessin_Zone_Couleur(
        -450*ECHELLE, -1000*ECHELLE, 100*ECHELLE, 300*ECHELLE, GR
    )   # CMC
    dessin_Zone_Couleur(
        -250*ECHELLE, -1000*ECHELLE, 100*ECHELLE, 300*ECHELLE, RD
    )   # CMC
    dessin_Zone_Couleur(
        150*ECHELLE, -1000*ECHELLE, 100*ECHELLE, 300*ECHELLE, GR
    )   # CMC
    dessin_Zone_Couleur(
        350*ECHELLE, -1000*ECHELLE, 100*ECHELLE, 300*ECHELLE, RD
    )   # CMC

    # *ECHELLE
    dessin_Zone(-300, -200, 600, 400, BLC)  # Dessine le contour noir en CTC
    dessin_Gobies_init()
    turtle.title("Simulation de la coupe")
    turtle.home()   # Retourne en 0;0 CTC


###############################################################################
if __name__ == '__main__':
    # dessin_Gobies_init()
    drawboard()
    turtle.mainloop()
