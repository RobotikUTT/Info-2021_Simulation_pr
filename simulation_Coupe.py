from random import randint
import turtle
from constantes import LISTEGOBI
import init_board
import robot_mouvment

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

# Crée le plateau de jeu
init_board.drawboard()
# Initialise le robot et les pinces
robot_mouvment.init_robot()

robot_mouvment.rotate(RGH, 90)
robot_mouvment.avancer(50)
robot_mouvment.rotate(LFT, 90)
robot_mouvment.avancer(1000)

turtle.mainloop()
