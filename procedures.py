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
    robot_mouvment.rotate_target(0)
    robot_mouvment.goto(2000, 1200, 180)
