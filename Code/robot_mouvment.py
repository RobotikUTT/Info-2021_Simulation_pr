import turtle
from random import randint
import math
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, BOTCOLOR, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO, ORIGINtBxB,
    ORIGINtByB, LONGUER_ACCEPTATION_PINCES, ORIGINtBxJ, ORIGINtByJ
)
import init_board

###############################################################################
"""
Ce fichier contient les fonctions relatives au mouvements
et actions du robot
"""
###############################################################################

STATE_PINCE1 = None
STATE_PINCE2 = None         # None signifie qu'elle est vide.
turtle.colormode(0xFF)

Robotik = turtle.Turtle()     # Crée le robot
pince1 = turtle.Turtle()    # Crée la pince1
pince2 = turtle.Turtle()    # Crée la pince2

###############################################################################

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
    xTB = Robotik.xcor()  # Valeur x de la coordonné de Robotik en CTC
    yTB = Robotik.ycor()  # Valeur y de la coordonné de Robotik en CTC
    alphTB = Robotik.heading()    # Donne un angle en degré entre 0 et 360
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

###############################################################################

def avancer(distance):
    """
    Cette fonction prend en paramètre une distance en mm
    Il fait avancer l'objet Robotik de "distance" et associant les pinces aux
    mouvement et vérifie si les pinces capturent un gobi.
    """
    # Met la distance en mm à l'échelle CTC et arondit
    distance = round(distance*ECHELLE)
    for i in range(distance):
        Robotik.forward(1)
        calculer_pos_pinces()
        prise_gobi()


def reculer(distance):
        """
        Cette fonction prend en paramètre une distance en mm
        Il fait reculer l'objet Robotik de "distance" et associant
        les pinces aux mouvement et vérifie si les pinces capturent un gobi.
        """
        # Met la distance en mm à l'échelle CTC et arondit
        distance = round(distance*ECHELLE)
        for i in range(distance):
            Robotik.backward(1)
            calculer_pos_pinces()

def rotate(sens, valeur):
    """
    Sens est soit égal à "left" soit égal à "right"
    valeur est degré.
    Robotik va tourner dans le sens et d'une valeur donnée
    """
    if sens == "left":
        for i in range(valeur):
            Robotik.left(1)
            calculer_pos_pinces()
            # prise_gobi()
            # On dit que le robot ne peut prendre un gobi en tournant
    elif sens == "right":
        for i in range(valeur):
            Robotik.right(1)
            calculer_pos_pinces()
            # prise_gobi()
            # On dit que le robot ne peut prendre un gobi en tournant


def rotate_target(angle):
    """
    Permet au robot de se positioner dans un angle précis par rapport à l'axe
    de base.
    Valeur doit être en degré entre 0 et 360.
    """
    if Robotik.heading() < angle:
        delta = angle - Robotik.heading()
        if delta < 180:
            rotate(LFT,int(delta))
        else:
            rotate(RGH, int(360-delta))
    elif Robotik.heading() > angle:
        delta = Robotik.heading() - angle
        if delta < 180:
            rotate(RGH, int(delta))
        else:
            rotate(LFT, int(360-delta))
    else:
        pass


def goto(xTarget, yTarget, tt = Robotik):
    """
    Cette fonction permet de donner une postion CMO et Robotik s'y rend.
    xTarget et yTarget sont les coordonnées du point visé
    Robot permet de séléctioner quel élément du robot on met en point de repère.
    """
    delta = 2*ENTRAX*math.cos(math.pi/6)
    angleEnPlus = 17
    eI = 93.45  # Distance entre pinc et point voulu après rotation

    xTarget = convert_CMOtoCTC(xTarget, "x")
    yTarget = convert_CMOtoCTC(yTarget, "y")

    """
    if tt == pince1:
        if Robotik.xcor() > xTarget:
            # The target is 'left' to Robotik
            xTarget = xTarget - ENTRAX*ECHELLE
        elif Robotik.xcor() < xTarget:
            # The target is 'right' to Robotik
            xTarget = xTarget + ENTRAX*ECHELLE
    elif tt == pince2:
        if Robotik.xcor() > yTarget:
            # The target is 'left' to Robotik
            yTarget = yTarget - ENTRAX*ECHELLE
        elif Robotik.xcor() < yTarget:
            # The target is 'right' to Robotik
            yTarget = xTarget + ENTRAX*ECHELLE
    else:
        pass
    """

    #Distanc absolue entre les coordonnés selon y
    distX = abs(xTarget - Robotik.xcor())
    #Distanc absolue entre les coordonnés selon y
    distY = abs(yTarget - Robotik.ycor())
    #Distanc absolue réduite à 15% entre les coordonnés selon x
    # distXRed = (distX-((15*distX)/100))
    phi = int((180*math.atan(distY/distX))/math.pi)
    # phiRed = (180*(math.atan(distY/distXRed)))/math.pi

    """
    print("*")
    print(xTarget)
    print(yTarget)
    print(Robotik.xcor())
    print(Robotik.ycor())
    print(distX)
    print(distY)
    print(phi)
    print("*")
    """

    if Robotik.xcor() > xTarget:
        # The target is 'left' to Robotik
        if Robotik.ycor() > yTarget:
            # The target is 'left-down' to Robotik
            rotate_target(int(180+phi))
            avancer(math.sqrt(distX*distX+distY*distY)/ECHELLE - delta)
            if tt == pince1:
                rotate(RGH, angleEnPlus)
                avancer(eI)
            elif tt == pince2:
                rotate(LFT, angleEnPlus)
                avancer(eI)
            else:
                avancer(delta)
        elif Robotik.ycor() < yTarget:
            # The target is 'left-up' to Robotik
            rotate_target(int(180-phi))
            avancer(math.sqrt(distX*distX+distY*distY)/ECHELLE - delta)
            if tt == pince1:
                rotate(RGH, angleEnPlus)
                avancer(eI)
            elif tt == pince2:
                rotate(LFT, angleEnPlus)
                avancer(eI)
            else:
                avancer(delta)
        else:
            # The target and Robotik are on the same y value
            rotate_target(int(180))
            avancer(int(abs(xTarget-Robotik.xcor())))

    elif Robotik.xcor() < xTarget:
        # The target is 'right' to Robotik
        if Robotik.ycor() > yTarget:
            # The target is 'right-down' to Robotik
            rotate_target(int(360-phi))
            avancer(math.sqrt(distX*distX+distY*distY)/ECHELLE - delta)
            if tt == pince1:
                rotate(RGH, angleEnPlus)
                avancer(eI)
            elif tt == pince2:
                rotate(LFT, angleEnPlus)
                avancer(eI)
            else:
                avancer(delta)
        elif Robotik.ycor() < yTarget:
            # The target is 'right-up' to Robotik
            rotate_target(int(phi))
            avancer(math.sqrt(distX*distX+distY*distY)/ECHELLE - delta)
            if tt == pince1:
                rotate(RGH, angleEnPlus)
                avancer(eI)
            elif tt == pince2:
                rotate(LFT, angleEnPlus)
                avancer(eI)
            else:
                avancer(delta)
        else:
            # The target and Robotik are on the same y value
            rotate_target(0)
            avancer(int(abs(xTarget-Robotik.xcor())))

    else:
        # The target and Robotik are on the same x value
        if Robotik.ycor() > yTarget:
            # The target is 'under' Robotik
            rotate(RGH, 90)
            avancer(int(abs(yTarget-Robotik.ycor())))
        elif Robotik.ycor() < yTarget:
            # The target is 'above' Robotik
            rotate(LFT, 90)
            avancer(int(abs(yTarget-Robotik.ycor())))
        else:
            return(1)   # Robotik is on the rigth place

###############################################################################

def prise_gobi():
    """
    Cette fonction va vérifier en fonction de la position des pinces si un gobi
    est pris.
    Un gobi est pris si la pince est vide et à la même position qu'un gobi.

    On appelle avec STATE_PINCE1 et STATE_PINCE2 qui sont de base à None donc
    ETATP1 et ETATP2 aussi.
    """
    global STATE_PINCE1, STATE_PINCE2
    if STATE_PINCE1 is None:
        prise = False
        compt = 0
        # on sort du while si compt = 24 ou si on est sur la position d'un gobi
        # pince1.xcor() est en CTC on applique ECHELLE à LISTEGOBI[compt][0]
        # et LISTEGOBI[compt][1]
        # On considère qu'une pince est sur postion d'un gobi si elle se trouve
        while not prise and compt < len(LISTEGOBI):
            if (
                abs(
                    convert_CMOtoCTC(LISTEGOBI[compt][0], "x") - pince1.xcor()
                ) <= LONGUER_ACCEPTATION_PINCES*ECHELLE
                and
                abs(
                    convert_CMOtoCTC(LISTEGOBI[compt][1], "y") - pince1.ycor()
                ) <= LONGUER_ACCEPTATION_PINCES*ECHELLE
            ):
                prise = True
            else:
                compt = compt + 1
        # Si prise = true alors la pince se trouve sur un gobi
        if prise:
            STATE_PINCE1 = LISTEGOBI[compt]
            # La pince prend la couleur du gobi
            pince1.fillcolor(STATE_PINCE1[2])
            # On efface le gobi avec la couleur du fond
            init_board.dessin_Cercle(
                convert_CMOtoCTC(LISTEGOBI[compt][0], "x"),
                convert_CMOtoCTC(LISTEGOBI[compt][1], "y"),
                AQA
            )
            del LISTEGOBI[compt]
    if STATE_PINCE2 is None:
        prise = False
        compt = 0
        while not prise and compt < len(LISTEGOBI):
            if (
                abs(
                    convert_CMOtoCTC(LISTEGOBI[compt][0], "x") - pince2.xcor()
                ) <= LONGUER_ACCEPTATION_PINCES*ECHELLE
                and
                abs(
                    convert_CMOtoCTC(LISTEGOBI[compt][1], "y") - pince2.ycor()
                ) <= LONGUER_ACCEPTATION_PINCES*ECHELLE
            ):
                prise = True
            else:
                compt = compt + 1
        if prise:
            STATE_PINCE2 = LISTEGOBI[compt]
            pince2.fillcolor(STATE_PINCE2[2])
            init_board.dessin_Cercle(
                convert_CMOtoCTC(LISTEGOBI[compt][0], "x"),
                convert_CMOtoCTC(LISTEGOBI[compt][1], "y"),
                AQA
            )
            del LISTEGOBI[compt]

def poser_gobi(tt):
    """
    Cette fonction va définir la position des zones vertes et rouges pour
    déposer les gobies. La fonction va ensuite tester si la position des pinces
    pleines correspond avec celle des zones de dépots.
    """
    global STATE_PINCE1, STATE_PINCE2
    if tt == pince1:
        pince1.fillcolor(255, 255, 255)
        init_board.dessin_Cercle(
        pince1.xcor(), pince1.ycor(), STATE_PINCE1[2]
        )
        LISTEGOBI.append((
            convert_CTCtoCMO(pince1.xcor(), "x"),
            convert_CTCtoCMO(pince1.ycor(), "y"),
            STATE_PINCE1[2], STATE_PINCE1[3])
        )
        STATE_PINCE1 = None
        reculer(100)
    if tt == pince2:
        pince2.fillcolor(255, 255, 255)
        init_board.dessin_Cercle(
        pince2.xcor(), pince2.ycor(), STATE_PINCE2[2]
        )
        LISTEGOBI.append((
            convert_CTCtoCMO(pince2.xcor(), "x"),
            convert_CTCtoCMO(pince2.ycor(), "y"),
            STATE_PINCE2[2], STATE_PINCE2[3])
        )
        STATE_PINCE2 = None
        reculer(100)
    else:
        pass

###############################################################################

# Initialise le Robotik et ses pinces
def init_robot(side):
    """
    Une fonction à n'utiliser d'une fois pour inintialiser le robot et les
    pinces.
    """

    Robotik.shape("square")
    Robotik.shapesize(2.4, 2.4, 1)
    Robotik.penup()
    Robotik.fillcolor(BOTCOLOR)

    pince1.shapesize(1, 1, 1)
    pince1.penup()
    pince1.fillcolor("white")
    pince1.shape("circle")

    pince2.shapesize(1, 1, 1)
    pince2.penup()
    pince2.fillcolor("white")
    pince2.shape("circle")

    # Enter the side of the robot

    if side == 'B':
        Robotik.goto(convert_CMOtoCTC(ORIGINtBxB,"x"),
            convert_CMOtoCTC(ORIGINtByB, "y")
        )
    elif side == 'J':
        Robotik.goto(convert_CMOtoCTC(ORIGINtBxJ,"x"),
            convert_CMOtoCTC(ORIGINtByJ, "y")
        )
        rotate_target(180)
    calculer_pos_pinces()

if __name__ == '__main__':
    init_robot()
    turtle.mainloop()
