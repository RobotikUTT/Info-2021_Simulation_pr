from random import randint
import turtle
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO, ORIGINtBxB,
    ORIGINtByB, ORIGINtBxJ, ORIGINtByJ
)
import init_board
import robot_mouvment

###############################################################################
""" Ce fichier contient les procédures de communications complexes"""
###############################################################################


def process_instruction():
    """
    Lance une console qui propsoe de rentrer une suite s'instruction en
    coordonnés (x;y) CMO et les convertit en un fichier lisible par
    la simulation. Crée le ficher pyS.txt
    Retourne le nombre de coordonnées totales.
    """
    quit = "Rest"
    nbrCoord = 0
    with open("pySim.txt", "w") as fl:
        print("Print 'Quit' to quit.\n")
        invite = input("\nEnter x :")
        while invite != "Quit":
            # Ecrit dans le fichier
            fl.write(invite+"\n"+input("\nEnter y :")+"\n")
            invite = input("\nEnter x :")
            nbrCoord += 1
    return(nbrCoord)


def read_instruction(nbrCoord):
    """
    Read the 'pyS.txt' file and convert it into goto intructions
    """
    with open("pySim.txt", "r") as fl:
        coord = fl.readlines()
        print(coord)
        nbr = 0
        while nbr < nbrCoord*2:
            x = int(coord[nbr].removesuffix('\n'))
            y = int(coord[nbr+1].removesuffix('\n'))
            nbr = nbr + 2
            print(x)
            print(y)
            robot_mouvment.goto(x, y)


def calcul_bot_mouv(coord, side):
    """
    Trouver quel est le déplacement objectif du robot en fonction de
    ceux demandées
    """
    compt = 0
    tup = []
    for i in coord:
        if compt % 2 == 0:
            if side == 'B':
                tup.append(i-ORIGINtBxB)
            elif side == 'J':
                tup.append(-(i-ORIGINtBxJ))
        else:
            if side == 'B':
                tup.append(-(i-ORIGINtByB))
            elif side == 'J':
                tup.append(i-ORIGINtByJ)
        compt = compt + 1
    return(tuple(tup))


def convert_instruction(number, side):
    """
    Ce fichier convertit en fichier .c les intructions du fichier 'pyS.txt'.
    Ce fichier sera lu par la carte arduino.
    """
    # Constantes pour l'écriture du fichier.c
    # nom du fichier : instructionList.h
    COMMENTSTRING = (
        "/*\n * \\ file instructionList.h\n * \\created by the simulation\n*/"
    )
    HEADSTRING = "#ifndef INSTRUCTIONLIST_H\n#define INSTRUCTIONLIST_H"
    FOOTSTRING = "#endif // INSTRUCTIONLIST_H"
    declare1 = "int nbrGoto = "
    declare2 = "int golist = ["

    with open('instructionList.h', 'w') as isC:
        # Ecrit la tête du fichier
        isC.write(COMMENTSTRING + "\n\n\n" + HEADSTRING + "\n\n" + declare2)
        # Lit l'ensemble du fichier dans un tableau pour chaque ligne
        pyS = open('pySim.txt', 'r')
        coord = pyS.readlines()
        pyS.close()
        # Retire les '\n' de chaque ligne et transforme en int
        for i in range(len(coord)):
            coord[i] = int(coord[i].removesuffix('\n'))
        coord = tuple(coord)
        coord = calcul_bot_mouv(coord, side)

        for xy in coord[:-1]:
            isC.write(str(xy) + ", ")   # Ecrit dans le tableau de coordonnés
        isC.write(
            str(coord[-1]) + "];\n" + declare1 + str(number) +
            ";\n\n" + FOOTSTRING
        )   # fini le fichier
