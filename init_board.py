import turtle
from random import randint
gr = "green"
rd = "red"
ble = "blue"
yl = "yellow"
blc = "black"


def dessinCercle(x, y, color):
    turtle.goto(x, y)
    turtle.pen(pencolor=color, fillcolor=color)
    turtle.begin_fill()
    turtle.circle(5)
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
    dessin_Zone(-300, -200, 600, 400, blc)
    # dessiner la zone de jeu1
    dessin_Zone(-300, -14, 80, 108, ble)
    # dessiner la zone de jeu2
    dessin_Zone(220, -14, 80, 108, yl)
    # dessiner la zone de jeu jaune bas
    dessin_Zone(-70, -200, 20, 60, yl)
    # dessiner la zone de jeu bleu bas
    dessin_Zone(50, -200, 20, 60, ble)
    ###############################################
    # dessiner les rochers
    dessin_Zone(-122.2, -200, 4.4, 30, blc)
    dessin_Zone(117.8, -200, 4.4, 30, blc)
    dessin_Zone(-2.2, -200, 4.4, 60, blc)
    ###############################################
    # Zone verte blueside
    dessin_Zone_Couleur(-300, 94, 80, 6, gr)
    # Zone rouge blueside
    dessin_Zone_Couleur(-300, -20, 80, 6, rd)
    # Zone rouge yellowside
    dessin_Zone_Couleur(220, 94, 80, 6, rd)
    # Zone verte yellowside
    dessin_Zone_Couleur(220, -20, 80, 6, gr)
    # Zone verte bluebotside
    dessin_Zone_Couleur(-90, -200, 20, 60, gr)
    # Zone rouge bluebotside
    dessin_Zone_Couleur(-50, -200, 20, 60, rd)
    # Zone verte yellowbotside
    dessin_Zone_Couleur(30, -200, 20, 60, gr)
    # Zone rouge yellowbotside
    dessin_Zone_Couleur(70, -200, 20, 60, rd)
    ###############################################
    # Gobi sideblue base
    dessinCercle(-240, 120, rd)
    dessinCercle(-211, 97, gr)
    dessinCercle(-211, -17, rd)
    dessinCercle(-240, -40, gr)
    # Gobi sideyellow base
    dessinCercle(240, 120, gr)
    dessinCercle(211, 97, rd)
    dessinCercle(211, -17, gr)
    dessinCercle(240, -40, rd)
    # Gobi sideblue large
    dessinCercle(-166, 180, rd)
    dessinCercle(-108.8, 120, gr)
    dessinCercle(-80, 40, rd)
    dessinCercle(-48, -40, gr)
    # Gobi sideyellow large
    dessinCercle(166, 180, gr)
    dessinCercle(108.8, 120, rd)
    dessinCercle(80, 40, gr)
    dessinCercle(48, -40, rd)
    # Gobi Rochers sideyellow
    dessinCercle(-99, -191, rd)
    dessinCercle(-87, -131, gr)
    dessinCercle(-33, -131, rd)
    dessinCercle(-21, -191, gr)
    # Gobi Rochers sideblue
    dessinCercle(21, -191, rd)
    dessinCercle(33, -131, gr)
    dessinCercle(87, -131, rd)
    dessinCercle(99, -191, gr)
    turtle.home()
    ###############################################


if __name__ == '__main__':
    drawboard()
    turtle.mainloop()
