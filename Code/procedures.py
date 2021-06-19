from random import randint
import turtle
from constantes import (
    LISTEGOBI, GR, RD, AQA, BLE, YL, BLC, ECHELLE, LFT, RGH, ENTRAX,
    VALEUR_ROTATION_P1P2, convert_CMOtoCTC, convert_CTCtoCMO, ORIGINtBx,
    ORIGINtBy
)
import init_board
import robot_mouvment

###############################################################################
""" Ce fichier contient les procédures de déplacements complexes"""
###############################################################################


def convert_instruction(number):
    """
    Ce fichier convertit en fichier .c les intructions du fichier 'pySim.txt'.
    Ce fichier sera lu par la carte arduino.
    """

    # Constantes pour l'écriture du fichier.c
    # nom du fichier : instructionList.# HACK:
    COMMENTSTRING = (
        "/*\n * \\ file instructionList.h\n * \\created by the simulation\n*/"
    )
    HEADSTRING = "#ifndef INSTRUCTIONLIST_H\n#define INSTRUCTIONLIST_H"
    FOOTSTRING = "#endif // INSTRUCTIONLIST_H"

    declare1 = "int nbrGoto = "
    declare2 = "int golist = ["

    ptrfile = open("instructionList.h", "w")
    ptrfile.write(COMMENTSTRING)
    ptrfile.write("\n\n\n")
    ptrfile.write(HEADSTRING)
    ptrfile.write("\n\n")
    ptrfile.write(declare2)

    ptrfileread = open("pySim.txt", "r")
    for i in range(number*2-1):
        x = ptrfileread.readline()
        x = x[:-1]
        ptrfile.write(x)
        ptrfile.write(", ")
    x = ptrfileread.readline()
    x = x[:-1]
    ptrfile.write(x)
    ptrfile.write("];\n")
    ptrfile.write(declare1)
    ptrfile.write(str(number*2))
    ptrfile.write(";\n\n")
    ptrfile.write(FOOTSTRING)



def process_instruction():
    """
    Lance une console qui propsoe de rentrer une suite s'instruction en
    coordonnés x y CMO et les convertit en un fichier lisible par
    la simulation
    """
    fl = open("pySim.txt", "w")
    quit = "Rest"
    nbrCoord = 0

    print("Print 'Quit' to quit.\n")
    x = input("\nEnter x :")
    while x != "Quit":
        fl.write(x)
        fl.write("\n")
        fl.write(input("\nEnter y :"))
        fl.write("\n")
        x = input("\nEnter x :")
        nbrCoord += 1
    fl.close()

    return(nbrCoord)


def read_instruction(nbrCoord):
    """
    Read the 'pySim.txt' file and convert it into goto intructions
    """
    with open("pySim.txt", "r") as filin:
        for nbr in range(nbrCoord):
            x = filin.readline()
            x = x[:-1]
            x = int(x)
            print(x)
            y = filin.readline()
            y = y[:-1]
            y = int(y)
            print(y)
            robot_mouvment.goto(x, y)
