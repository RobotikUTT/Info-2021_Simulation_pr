import os
import turtle
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO, ORIGINtBxB,
    ORIGINtByB, ORIGINtBxJ, ORIGINtByJ
)
import init_board as ib
import robot_mouvment as rm
import procedures

os.system("cls")

ib.drawboard()  # Crée le plateau de jeux
# SIDE = input("Enter the side ('B' or 'J'): ")   # Choisit le côté de la table
# while SIDE != 'B' and SIDE != 'J':
    # SIDE = input("Enter the side ('B' or 'J'): ")
rm.init_robot()     # Initialise le robot et les pinces

invite = input("\nAction (A##, B##, R##S, T##, P#, S#): ")
while invite != 'Quit':
    print(invite)
    act = invite[0]
    val = invite[1:]

    if act == 'A':
        rm.avancer(float(val))
    elif act == 'R':
        sens = val[-1]
        val = int(val[:-1])
        if sens == 'G':
            rm.rotate('left', val)
        else:
            rm.rotate('right', val)
    elif act == 'B':
        rm.reculer(float(val))
    elif act == 'T':
        rm.rotate_target(int(val))
    elif act == 'P':
        rm.prise_gobi(int(val))
    elif act == 'S':
        rm.poser_gobi(int(val))
    else:
        print("\nNo")

    invite = input("\nAction (A##, R##S, B##, T##): ")
else:
    turtle.mainloop()
