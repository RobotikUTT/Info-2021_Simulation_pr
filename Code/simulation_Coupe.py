from random import randint
import turtle
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO, ORIGINtBxB,
    ORIGINtByB, ORIGINtBxJ, ORIGINtByJ
)
import init_board
import robot_mouvment
import procedures

###############################################################################
""" Ce fichier est l'executable de la simulation, c'est ici que le code final
est compilé pour la simulation """
###############################################################################

# Crée le plateau de jeu
init_board.drawboard()
# Initialise le robot et les pinces
robot_mouvment.init_robot()
# process_instruction()
x = procedures.process_instruction()
procedures.read_instruction(x)
procedures.convert_instruction(x)

turtle.mainloop()
