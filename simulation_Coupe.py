from random import randint
import turtle
from constantes import LISTEGOBI
import init_board
import robot_mouvment

# Crée le plateau de jeu
init_board.drawboard()
# Initialise le robot et les pinces
robot_mouvment.init_robot()



turtle.mainloop()
