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


def convert_instruction():
    """
    Ce fichier convertit en fichier .c les intructions du fichier 'pySim.txt'.
    Ce fichier sera lu par la carte arduino.
    """


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


def parcour1():
    robot_mouvment.rotate(LFT, 45)
    robot_mouvment.avancer(180)
    print(LISTEGOBI)
    robot_mouvment.rotate(RGH, 90)
    robot_mouvment.avancer(80)
    robot_mouvment.rotate(LFT, 45)
    robot_mouvment.avancer(800)
    print(LISTEGOBI)
    robot_mouvment.poser_gobi(2)
    robot_mouvment.reculer(500)
    print(LISTEGOBI)
    robot_mouvment.avancer(600)
    print(LISTEGOBI)
    robot_mouvment.avancer(100)
    robot_mouvment.rotate(LFT, 180)
    robot_mouvment.avancer(900)
    print(LISTEGOBI)
    robot_mouvment.rotate(LFT, 90)
    robot_mouvment.avancer(250)
    robot_mouvment.poser_gobi(2)
    print(LISTEGOBI)
    robot_mouvment.rotate(LFT, 180)
    robot_mouvment.avancer(250)
    robot_mouvment.poser_gobi(1)
    print(LISTEGOBI)


def parcourTest():
    """
    robot_mouvment.goto(956, 400, tt=robot_mouvment.pince1)
    robot_mouvment.goto(1900, 800, tt=robot_mouvment.pince2)
    robot_mouvment.goto(ORIGINtBx, ORIGINtBy)
    robot_mouvment.goto(ORIGINtBx, 515, tt=robot_mouvment.pince1)
    robot_mouvment.poser_gobi(robot_mouvment.pince1)
    """
    # process_instruction()
    read_instruction(process_instruction())
