import turtle
from random import randint
from constantes import LISTEGOBI

###############################################################################
GR = "green"
RD = "red"
BLE = "blue"
YL = "yellow"
BLC = "black"
ECHELLE = 1/5
LFT = "left"
RGH = "right"
ENTRAX = 117.95     # En mm
VALEUR_ROTATION_P1P2 = 30.0
###############################################################################


def dessin_Gobies_init():
    for i in range(0, 24):
        dessin_Cercle(
            LISTEGOBI[i][0]*ECHELLE, LISTEGOBI[i][1]*ECHELLE, LISTEGOBI[i][2]
        )


def dessin_Cercle(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pen(pencolor=color, fillcolor=color)
    turtle.begin_fill()
    turtle.circle(6.2)
    turtle.end_fill()


def dessin_Zone_Couleur(x, y, long, large, color):
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
    turtle.bgcolor("aqua")
    turtle.speed(100)
    turtle.shapesize(0.1, 0.1, 0.1)
    turtle.penup()

    # dessiner le cadre
    dessin_Zone(-300, -200, 600, 400, BLC)
    # dessiner la zone de jeu1
    dessin_Zone(-300, -14, 80, 108, BLE)
    # dessiner la zone de jeu2
    dessin_Zone(220, -14, 80, 108, YL)
    # dessiner la zone de jeu jaune bas
    dessin_Zone(-70, -200, 20, 60, YL)
    # dessiner la zone de jeu bleu bas
    dessin_Zone(50, -200, 20, 60, BLE)
    # dessiner les rochers
    dessin_Zone(-122.2, -200, 4.4, 30, BLC)
    dessin_Zone(117.8, -200, 4.4, 30, BLC)
    dessin_Zone(-2.2, -200, 4.4, 60, BLC)
    # dessiner les zones de couleurs des bases
    dessin_Zone_Couleur(
        -1500*ECHELLE, 470*ECHELLE, 400*ECHELLE, 30*ECHELLE, GR
    )
    dessin_Zone_Couleur(
        -1500*ECHELLE, -100*ECHELLE, 400*ECHELLE, 30*ECHELLE, RD
    )
    dessin_Zone_Couleur(
        1100*ECHELLE, 470*ECHELLE, 400*ECHELLE, 30*ECHELLE, RD
    )
    dessin_Zone_Couleur(
        1100*ECHELLE, -100*ECHELLE, 400*ECHELLE, 30*ECHELLE, GR
    )
    # dessiner les zones de couleurs des bases rochers
    dessin_Zone_Couleur(
        -450*ECHELLE, -1000*ECHELLE, 100*ECHELLE, 300*ECHELLE, GR
    )
    dessin_Zone_Couleur(
        -250*ECHELLE, -1000*ECHELLE, 100*ECHELLE, 300*ECHELLE, RD
    )
    dessin_Zone_Couleur(
        150*ECHELLE, -1000*ECHELLE, 100*ECHELLE, 300*ECHELLE, GR
    )
    dessin_Zone_Couleur(
        350*ECHELLE, -1000*ECHELLE, 100*ECHELLE, 300*ECHELLE, RD
    )

    # *ECHELLE

    dessin_Gobies_init()
    turtle.title("Simulation de la coupe")
    turtle.home()


###############################################################################
if __name__ == '__main__':
    # dessin_Gobies_init()
    drawboard()
    turtle.mainloop()
