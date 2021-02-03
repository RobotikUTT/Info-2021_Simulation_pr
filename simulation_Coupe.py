import turtle
from random import randint

# Crée le plateau de jeu
import init_board
init_board.drawboard()

# Nomme la fenêtre
turtle.title("Simulation de la coupe")

tBleu = turtle.Turtle()
tBleu.shape("square")
tBleu.shapesize(2.2, 2.2, 2.2)

# Place le curseur tBleu en départ gauche
tBleu.penup()
tBleu.goto(-250, 40)
tBleu.fillcolor("blue")

turtle.mainloop()
