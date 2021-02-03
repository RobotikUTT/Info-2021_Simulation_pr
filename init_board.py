import turtle
from random import randint
GR = "green"
RD = "red"
BLE = "blue"
YL = "yellow"
BLC = "black"
ECHELLE = 1/5
LISTEGOBI = [
    (-1200*ECHELLE, 600*ECHELLE, RD, "QB1"),
    (-1055*ECHELLE, 485*ECHELLE, GR, "QB2"),
    (-1055*ECHELLE, -85*ECHELLE, RD, "QB3"),
    (-1200*ECHELLE, -200*ECHELLE, GR, "QB4"),
    (1200*ECHELLE, 600*ECHELLE, GR, "QJ1"),
    (1055*ECHELLE, 485*ECHELLE, RD, "QJ2"),
    (1055*ECHELLE, -85*ECHELLE, GR, "QJ3"),
    (1200*ECHELLE, -200*ECHELLE, RD, "QJ4"),
    (-830*ECHELLE, 900*ECHELLE, RD, "LB1"),
    (-544*ECHELLE, 600*ECHELLE, GR, "LB2"),
    (-400*ECHELLE, 200*ECHELLE, RD, "LB3"),
    (-230*ECHELLE, -200*ECHELLE, GR, "LB4"),
    (830*ECHELLE, 900*ECHELLE, GR, "LJ1"),
    (544*ECHELLE, 600*ECHELLE, RD, "LJ2"),
    (400*ECHELLE, 200*ECHELLE, GR, "LJ3"),
    (230*ECHELLE, -200*ECHELLE, RD, "LJ4"),
    (-495*ECHELLE, -955*ECHELLE, RD, "CB1"),
    (-435*ECHELLE, -655*ECHELLE, GR, "CB2"),
    (-165*ECHELLE, -655*ECHELLE, RD, "CB3"),
    (-105*ECHELLE, -955*ECHELLE, GR, "CB4"),
    (105*ECHELLE, -955*ECHELLE, RD, "CJ1"),
    (165*ECHELLE, -655*ECHELLE, GR, "CJ2"),
    (435*ECHELLE, -655*ECHELLE, RD, "CJ3"),
    (495*ECHELLE, -955*ECHELLE, GR, "CJ4"),
]
# Donc la liste va de 0 à 23, avec 0 à 3 dans les sous toples
###############################################################################


def dessin_Gobies_init():
    for i in range(0, 24):
        dessin_Cercle(LISTEGOBI[i][0], LISTEGOBI[i][1], LISTEGOBI[i][2])


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

    dessin_Gobies_init()
    turtle.home()


###############################################################################
if __name__ == '__main__':
    # dessin_Gobies_init()
    drawboard()
    turtle.mainloop()
