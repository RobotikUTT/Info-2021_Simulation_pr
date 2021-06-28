import os
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

os.system("cls")

init_board.drawboard()  # Crée le plateau de jeu

# Choisit le côté de la table
SIDE = input("Enter the side ('B' or 'J'): ")
while SIDE != 'B' and SIDE != 'J':
    SIDE = input("Enter the side ('B' or 'J'): ")

robot_mouvment.init_robot(SIDE)     # Initialise le robot et les pinces

nbrCoord = procedures.process_instruction()    # process_instruction()
procedures.read_instruction(nbrCoord)
# procedures.convert_instruction(nbrCoord, SIDE)

turtle.mainloop()
