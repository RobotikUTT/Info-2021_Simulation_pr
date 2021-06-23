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
        for nbr in range(nbrCoord):
            x = int(coord[nbr].removesuffix('\n'))
            y = int(coord[nbr+1].removesuffix('\n'))
            nbr = nbr + 1
            robot_mouvment.goto(x, y)


def convert_instruction(number):
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

    with open("instructionList.h", "w") as isC:
        # Ecrit la tête du fichier
        isC.write(COMMENTSTRING + "\n\n\n" + HEADSTRING + "\n\n" + declare2)

        with open("pySim.txt", "r") as pyS:
            for i in range(number*2-1):
                x = pyS.readline()
                isC.write(x.removesuffix('\n'))
                isC.write(", ")

            # Ecrit la fin du fichier
            x = pyS.readline()
            isC.write(
                x.removesuffix('\n') + "];\n" + declare1 + str(number*2) +
                ";\n\n" + FOOTSTRING
            )
