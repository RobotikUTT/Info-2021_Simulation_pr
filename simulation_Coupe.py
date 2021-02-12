from random import randint
import turtle
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO
)
import init_board
import robot_mouvment


# Crée le plateau de jeu
init_board.drawboard()
# Initialise le robot et les pinces
robot_mouvment.init_robot()

robot_mouvment.rotate(RGH, 90)
robot_mouvment.avancer(100)
robot_mouvment.rotate(LFT, 90)
robot_mouvment.avancer(1000)

turtle.mainloop()
