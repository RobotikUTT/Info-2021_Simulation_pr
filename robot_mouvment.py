import turtle
from random import randint
import math
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, BOTCOLOR, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2
)
import init_board

###############################################################################
STATE_PINCE1 = None
STATE_PINCE2 = None         # Vrai signifie que la pince est libre
###############################################################################

# coordonnées turtle centrée = CTC
# coordonnées mm centrée = CMC
# coordonnées mm offset = CMO

def calculer_pos_pinces():
    """
    On peut retrouver différentes informations à l'aide des différentes
    fonctions turtle (lien) :
    https://docs.python.org/fr/3/library/turtle.html#tell-turtle-s-state
    On va donc détérminer le vecteur "vision" : v, du robot. Qui possède comme
    norme la valeur de ENTRAX et possède la même direction que la ligne de
    vision définit avec heading().
    On va ensuite définir les vecteur p1 et p2 qui sont égaux à
    v + une rotation.
    Les pinces se trouvent alors toujours à la tête de ces vecteurs p1 et p2.
    """
    xTB = tBlue.xcor()  # Valeur x de la coordonné de tBlue en CTC
    yTB = tBlue.ycor()  # Valeur y de la coordonné de tBlue en CTC
    alphTB = tBlue.heading()    # Donne un angle en degré entre 0 et 360
    # On définit le vecteur vision
    # Dans les 4 cas suivant le vecteur prend des valeurs remarquable
    if (alphTB == 0) or (alphTB == 360):
        v = turtle.Vec2D((ENTRAX*ECHELLE), 0)
    elif alphTB == 90:
        v = turtle.Vec2D(0, (ENTRAX*ECHELLE))
    elif alphTB == 180:
        v = turtle.Vec2D(-(ENTRAX*ECHELLE), 0)
    elif alphTB == 270:
        v = turtle.Vec2D(0, -(ENTRAX*ECHELLE))
    else:
        # On fait un peu de trigo pour trouver les coordonnés de v à partir de
        # deux valeurs intermédiaires m et n.
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
    # On crée p1 et p2
    p1 = v
    p2 = v
    p1 = p1.rotate(VALEUR_ROTATION_P1P2)
    p2 = p2.rotate(-VALEUR_ROTATION_P1P2)
    # On connait l'origine des vecteurs p1 et p2
    # On cherche alors l'arrivé, la tête
    xp1 = p1[0] + xTB
    yp1 = p1[1] + yTB
    xp2 = p2[0] + xTB
    yp2 = p2[1] + yTB
    pince1.penup()
    pince1.goto(xp1, yp1)
    pince2.penup()
    pince2.goto(xp2, yp2)


def avancer(distance):
    """
    Cette fonction prend en paramètre une distance en mm
    Il fait avancer l'objet tBlue de "distance" et associant les pinces aux
    mouvement et vérifie si les pinces capturent un gobi.
    """
    # Met la distance en mm à l'échelle CTC et arondit
    distance = round(distance*ECHELLE)
    for i in range(distance):
        tBlue.forward(1)
        calculer_pos_pinces()
        prise_gobi(STATE_PINCE1, STATE_PINCE2)


def rotate(sens, valeur):
    """
    sens est soit égal à "left" soit égal à "right"
    valeur est est degré.
    tBlue va tourner dans le sens et d'une valeur donnée
    """
    # valeur = round(valeur*ECHELLE)
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
    if ETATP1 is None:
        prise = False
        compt = 0
        while not prise and compt < len(LISTEGOBI):
            if (
                abs(LISTEGOBI[compt][0]*ECHELLE - pince1.xcor()) <= 50*ECHELLE
                and
                abs(LISTEGOBI[compt][1]*ECHELLE - pince1.ycor()) <= 50*ECHELLE
            ):
                prise = True
            else:
                compt = compt + 1
        if prise:
            STATE_PINCE1 = LISTEGOBI[compt]
            pince1.fillcolor(STATE_PINCE1[2])
            init_board.dessin_Cercle(
                STATE_PINCE1[0]*ECHELLE, STATE_PINCE1[1]*ECHELLE,
                AQA
            )
    if ETATP2 is None:
        prise = False
        compt = 0
        while not prise and compt < len(LISTEGOBI):
            if (
                abs(LISTEGOBI[compt][0]*ECHELLE - pince2.xcor()) <= 10*ECHELLE
                and
                abs(LISTEGOBI[compt][1]*ECHELLE - pince2.ycor()) <= 10*ECHELLE
            ):
                prise = True
            else:
                compt = compt + 1
        if prise:
            STATE_PINCE2 = LISTEGOBI[compt]
            pince1.fillcolor(STATE_PINCE2[2])
            init_board.dessin_Cercle(
                STATE_PINCE2[0]*ECHELLE, STATE_PINCE2[1]*ECHELLE,
                AQA
            )
###############################################################################
# Initialise les tBlue et ses pinces


tBlue = turtle.Turtle()     # Crée le robot
pince1 = turtle.Turtle()    # Crée la pince1
pince2 = turtle.Turtle()    # Crée la pince2

if __name__ == '__main__':
    init_robot()
    turtle.mainloop()
