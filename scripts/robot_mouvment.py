import turtle
from random import randint
import math
import liste_gobies

tBlue = turtle.Turtle()     # Crée le robot
pince1 = turtle.Turtle()    # Crée la pince1
pince2 = turtle.Turtle()    # Crée la pince2
LFT = "left"
RGH = "right"
ENTRAX = 117.95     # En mm
ECHELLE = 1/5
VALEUR_ROTATION_P1P2 = 30.0
# Donc la liste va de 0 à 23, avec 0 à 3 dans les sous toples
###############################################################################


def calculer_pos_pinces():
    xTB = tBlue.xcor()
    yTB = tBlue.ycor()
    alphTB = tBlue.heading()
    if (alphTB == 0) or (alphTB == 360):
        v = turtle.Vec2D((ENTRAX*ECHELLE), 0)
    elif alphTB == 90:
        v = turtle.Vec2D(0, (ENTRAX*ECHELLE))
    elif alphTB == 180:
        v = turtle.Vec2D(-(ENTRAX*ECHELLE), 0)
    elif alphTB == 270:
        v = turtle.Vec2D(0, -(ENTRAX*ECHELLE))
    else:
        if (alphTB > 0 and alphTB < 90):
            m = math.cos(math.radians(alphTB))*(ENTRAX*ECHELLE)
            n = math.sin(math.radians(alphTB))*(ENTRAX*ECHELLE)
            v = turtle.Vec2D(m, n)
        elif (alphTB > 90 and alphTB < 180):
            alphTB = 180 - alphTB
            m = -math.cos(math.radians(alphTB))*(ENTRAX*ECHELLE)
            n = math.sin(math.radians(alphTB))*(ENTRAX*ECHELLE)
            v = turtle.Vec2D(m, n)
        elif (alphTB > 180 and alphTB < 270):
            alphTB = alphTB - 180
            m = -math.cos(math.radians(alphTB))*(ENTRAX*ECHELLE)
            n = -math.sin(math.radians(alphTB))*(ENTRAX*ECHELLE)
            v = turtle.Vec2D(m, n)
        elif (alphTB > 270 and alphTB < 360):
            alphTB = 360 - alphTB
            m = math.cos(math.radians(alphTB))*(ENTRAX*ECHELLE)
            n = -math.sin(math.radians(alphTB))*(ENTRAX*ECHELLE)
            v = turtle.Vec2D(m, n)
    p1 = v
    p2 = v
    p1 = p1.rotate(VALEUR_ROTATION_P1P2)
    p2 = p2.rotate(-VALEUR_ROTATION_P1P2)
    xp1 = p1[0] + xTB
    yp1 = p1[1] + yTB
    xp2 = p2[0] + xTB
    yp2 = p2[1] + yTB
    pince1.penup()
    pince1.goto(xp1, yp1)
    pince2.penup()
    pince2.goto(xp2, yp2)


def avancer(distance):
    distance = round(distance*ECHELLE)
    for i in range(distance):
        tBlue.forward(1)
        calculer_pos_pinces()


def rotate(sens, valeur):
    valeur = round(valeur*ECHELLE)
    if sens == "left":
        for i in range(valeur):
            tBlue.left(1)
            calculer_pos_pinces()
    elif sens == "right":
        for i in range(valeur):
            tBlue.right(1)
            calculer_pos_pinces()


def init_robot():
    tBlue.shape("square")
    tBlue.shapesize(2.2, 2.2, 2.2)
    tBlue.penup()
    tBlue.fillcolor("blue")

    pince1.shapesize(1, 1, 1)
    pince1.penup()
    pince1.fillcolor("white")
    pince1.shape("circle")

    pince2.shapesize(1, 1, 1)
    pince2.penup()
    pince2.fillcolor("white")
    pince2.shape("circle")

    tBlue.goto(-250, 40)
    calculer_pos_pinces()

###############################################################################
# Initialise les tBlue et ses pinces


if __name__ == '__main__':
    init_robot()
    turtle.mainloop()
