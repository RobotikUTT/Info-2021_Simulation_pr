import turtle
from random import randint
GR = "green"
RD = "red"
BLE = "blue"
YL = "yellow"
BLC = "black"
ECHELLE = 1/5
LISTE_GOBI = [
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
    (830, 900, BR, "LJ1"),
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
# Donc le tuple va de 0 à 71
###############################################################################


def dessinGobies():
    for i in range(0, 23, 2):
        r


def dessinCercle(x, y, color):
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
    ###############################################
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
    ###############################################
    # dessiner les rochers
    dessin_Zone(-122.2, -200, 4.4, 30, BLC)
    dessin_Zone(117.8, -200, 4.4, 30, BLC)
    dessin_Zone(-2.2, -200, 4.4, 60, BLC)
    ###############################################
    # Zone verte blueside
    dessin_Zone_Couleur(-300, 94, 80, 6, GR)
    # Zone rouge blueside
    dessin_Zone_Couleur(-300, -20, 80, 6, RD)
    # Zone rouge yellowside
    dessin_Zone_Couleur(220, 94, 80, 6, RD)
    # Zone verte yellowside
    dessin_Zone_Couleur(220, -20, 80, 6, GR)
    # Zone verte bluebotside
    dessin_Zone_Couleur(-90, -200, 20, 60, GR)
    # Zone rouge bluebotside
    dessin_Zone_Couleur(-50, -200, 20, 60, RD)
    # Zone verte yellowbotside
    dessin_Zone_Couleur(30, -200, 20, 60, GR)
    # Zone rouge yellowbotside
    dessin_Zone_Couleur(70, -200, 20, 60, RD)
    ###############################################
    # Gobi sideblue base
    dessinCercle(-240, 120, RD)
    dessinCercle(-211, 97, GR)
    dessinCercle(-211, -17, RD)
    dessinCercle(-240, -40, GR)
    # Gobi sideyellow base
    dessinCercle(240, 120, GR)
    dessinCercle(211, 97, RD)
    dessinCercle(211, -17, GR)
    dessinCercle(240, -40, RD)
    # Gobi sideblue large
    dessinCercle(-166, 180, RD)
    dessinCercle(-108.8, 120, GR)
    dessinCercle(-80, 40, RD)
    dessinCercle(-48, -40, GR)
    # Gobi sideyellow large
    dessinCercle(166, 180, GR)
    dessinCercle(108.8, 120, RD)
    dessinCercle(80, 40, GR)
    dessinCercle(48, -40, RD)
    # Gobi Rochers sideyellow
    dessinCercle(-99, -191, RD)
    dessinCercle(-87, -131, GR)
    dessinCercle(-33, -131, RD)
    dessinCercle(-21, -191, GR)
    # Gobi Rochers sideblue
    dessinCercle(21, -191, RD)
    dessinCercle(33, -131, GR)
    dessinCercle(87, -131, RD)
    dessinCercle(99, -191, GR)
    turtle.home()
    ###############################################


if __name__ == '__main__':
    drawboard()
    turtle.mainloop()
