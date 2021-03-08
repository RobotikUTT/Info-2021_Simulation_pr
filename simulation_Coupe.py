# Ici on a la Simulation j'écris

from random import randint
import turtle
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO, ORIGINtBx,
    ORIGINtBy
)
import init_board
import robot_mouvment


# Crée le plateau de jeu
init_board.drawboard()
# Initialise le robot et les pinces
robot_mouvment.init_robot()

robot_mouvment.rotate(LFT, 45)
robot_mouvment.avancer(180)
print(LISTEGOBI)
print("\n")
robot_mouvment.rotate(RGH, 90)
robot_mouvment.avancer(80)
robot_mouvment.rotate(LFT, 45)
robot_mouvment.avancer(800)
print(LISTEGOBI)
print("\n")
robot_mouvment.poser_gobi(2)
robot_mouvment.reculer(500)
print(LISTEGOBI)
print("\n")
robot_mouvment.avancer(600)
print(LISTEGOBI)
print("\n")
robot_mouvment.avancer(100)
robot_mouvment.rotate(LFT, 180)
robot_mouvment.avancer(900)
print(LISTEGOBI)
print("\n")
robot_mouvment.rotate(LFT, 90)
robot_mouvment.avancer(250)
robot_mouvment.poser_gobi(2)
print(LISTEGOBI)
print("\n")
robot_mouvment.rotate(LFT, 180)
robot_mouvment.avancer(250)
robot_mouvment.poser_gobi(1)
print(LISTEGOBI)
print("\n")
turtle.mainloop()
