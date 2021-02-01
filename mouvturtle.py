import turtle
from random import randint

tBleu.shape("square")
tJaune.shape("square")

turtle.mainloop()

#Place le curseur tBleu en départ gauche
tBleu.penup()
tBleu.goto(-240,40)
tBleu.fillcolor("blue")

#Place le curseur tJaune en départ gauche
tJaune.penup()
tJaune.goto(240,40)
tJaune.fillcolor("yellow")
tJaune.right(180)
