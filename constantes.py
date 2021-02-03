import turtle
import math
from random import randint

GR = "green"
RD = "red"
BLE = "blue"
YL = "yellow"
BLC = "black"
ECHELLE = 1/5
LFT = "left"
RGH = "right"
ENTRAX = 117.95     # En mm
VALEUR_ROTATION_P1P2 = 30.0

LISTEGOBI = [
    (-1200, 600, RD, "QB1"),
    (-1055, 485, GR, "QB2"),
    (-1055, -85, RD, "QB3"),
    (-1200, -200, GR, "QB4"),
    (1200, 600, GR, "QJ1"),
    (1055, 485, RD, "QJ2"),
    (1055, -85, GR, "QJ3"),
    (1200, -200, RD, "QJ4"),
    (-830, 900, RD, "LB1"),
    (-544, 600, GR, "LB2"),
    (-400, 200, RD, "LB3"),
    (-230, -200, GR, "LB4"),
    (830, 900, GR, "LJ1"),
    (544, 600, RD, "LJ2"),
    (400, 200, GR, "LJ3"),
    (230, -200, RD, "LJ4"),
    (-495, -955, RD, "CB1"),
    (-435, -655, GR, "CB2"),
    (-165, -655, RD, "CB3"),
    (-105, -955, GR, "CB4"),
    (105, -955, RD, "CJ1"),
    (165, -655, GR, "CJ2"),
    (435, -655, RD, "CJ3"),
    (495, -955, GR, "CJ4"),
]
# Donc la liste va de 0 à 23, avec 0 à 3 dans les sous toples
