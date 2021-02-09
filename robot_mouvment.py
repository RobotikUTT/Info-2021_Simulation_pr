import turtle
from random import randint
import math
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, BOTCOLOR, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2
)
import init_board

###############################################################################
STATE_PINCE1 = True
STATE_PINCE2 = True         # Vrai signifie que la pince est libre
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
        prise_gobi(STATE_PINCE1, STATE_PINCE2)


def rotate(sens, valeur):
    valeur = round(valeur*ECHELLE)
    if sens == "left":
        for i in range(valeur):
            tBlue.left(1)
            calculer_pos_pinces()
            prise_gobi(STATE_PINCE1, STATE_PINCE2)
    elif sens == "right":
        for i in range(valeur):
            tBlue.right(1)
            calculer_pos_pinces()
            prise_gobi(STATE_PINCE1, STATE_PINCE2)


def init_robot():
    tBlue.shape("square")
    tBlue.shapesize(2.2, 2.2, 2.2)
    tBlue.penup()
    tBlue.fillcolor(BOTCOLOR)

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
    print(pince1.position())
    print(pince2.position())


def prise_gobi(ETATP1, ETATP2):
    if ETATP1:
        prise = False
        compt = 0
        while not prise and compt <= 23:
            if (
                abs(LISTEGOBI[compt][0]*ECHELLE - pince1.xcor()) <= 50*ECHELLE
                and
                abs(LISTEGOBI[compt][1]*ECHELLE - pince1.ycor()) <= 50*ECHELLE
            ):
                prise = True
            else:
                compt = compt + 1
        if prise:
            pince1.fillcolor(LISTEGOBI[compt][2])
            init_board.dessin_Cercle(
                LISTEGOBI[compt][0]*ECHELLE, LISTEGOBI[compt][1]*ECHELLE,
                AQA
            )
            STATE_PINCE1 = False
    if ETATP2:
        prise = False
        compt = 0
        while not prise and compt <= 23:
            if (
                abs(LISTEGOBI[compt][0]*ECHELLE - pince2.xcor()) <= 50*ECHELLE
                and
                abs(LISTEGOBI[compt][1]*ECHELLE - pince2.ycor()) <= 50*ECHELLE
            ):
                prise = True
            else:
                compt = compt + 1
        if prise:
            pince2.fillcolor(LISTEGOBI[compt][2])
            init_board.dessin_Cercle(
                LISTEGOBI[compt][0]*ECHELLE, LISTEGOBI[compt][1]*ECHELLE,
                AQA
            )
            STATE_PINCE2 = False
###############################################################################
# Initialise les tBlue et ses pinces


tBlue = turtle.Turtle()     # Crée le robot
pince1 = turtle.Turtle()    # Crée la pince1
pince2 = turtle.Turtle()    # Crée la pince2

if __name__ == '__main__':
    init_robot()
    turtle.mainloop()
