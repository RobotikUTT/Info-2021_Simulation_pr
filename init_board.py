import turtle
from random import randint

tBleu= turtle.Turtle()
tJaune = turtle.Turtle()

turtle.bgcolor("aqua")
turtle.title("Plateau de la coupe")
turtle.speed(100)
turtle.shapesize(0.1,0.1,0.1)

###############################################

#dessiner le cadre
turtle.penup()
turtle.goto(-300,200)
turtle.pendown()
turtle.goto(300,200)
turtle.goto(300,-200)
turtle.goto(-300,-200)
turtle.goto(-300,200)
turtle.penup()

#dessiner la zone de jeu1
turtle.goto(-300,100)
turtle.pen(pencolor="blue")
turtle.pendown()
turtle.goto(-220,100)
turtle.goto(-220,-20)
turtle.goto(-300,-20)
turtle.pen(pencolor="black")
turtle.penup()

#dessiner la zone de jeu2
turtle.goto(300,100)
turtle.pen(pencolor="yellow")
turtle.pendown()
turtle.goto(220,100)
turtle.goto(220,-20)
turtle.goto(300,-20)
turtle.pen(pencolor="black")
turtle.penup()

turtle.goto(-70,-200)
turtle.pen(pencolor="yellow")
turtle.pendown()
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.pen(pencolor="black")
turtle.penup()

turtle.goto(50,-200)
turtle.pen(pencolor="blue")
turtle.pendown()
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.pen(pencolor="black")
turtle.penup()

#############################################################""

#dessiner les rochers
turtle.goto(-122.2,-200)
turtle.pendown()
turtle.goto(-122.2,-170)
turtle.goto(-117.8,-170)
turtle.goto(-117.8,-200)
turtle.penup()

turtle.goto(117.8,-200)
turtle.pendown()
turtle.goto(117.8,-170)
turtle.goto(122.2,-170)
turtle.goto(122.2,-200)
turtle.penup()

turtle.goto(-2.2,-200)
turtle.pendown()
turtle.goto(-2.2,-140)
turtle.goto(2.2,-140)
turtle.goto(2.2,-200)
turtle.penup()

######################################################""

#Zone verte blueside
turtle.goto(-300,94)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.forward(80)
turtle.left(90)
turtle.forward(6)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(6)
turtle.left(90)
turtle.end_fill()

#Zone rouge blueside
turtle.goto(-300,-14)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.forward(80)
turtle.right(90)
turtle.forward(6)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(6)
turtle.right(90)
turtle.end_fill()

#Zone rouge yellowside
turtle.goto(220,94)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.forward(80)
turtle.left(90)
turtle.forward(6)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(6)
turtle.left(90)
turtle.end_fill()

#Zone verte yellowside
turtle.goto(220,-14)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.forward(80)
turtle.right(90)
turtle.forward(6)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(6)
turtle.right(90)
turtle.end_fill()

###################################################################################

#Zone verte bluebotside
turtle.goto(-90,-200)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.end_fill()

#Zone rouge bluebotside
turtle.goto(-50,-200)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.end_fill()

#Zone verte yellowbotside
turtle.goto(30,-200)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.end_fill()

#Zone rouge yellowbotside
turtle.goto(70,-200)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.end_fill()

########################################################################################

#dessiner les gobis
#t.pen(pencolor="purple", fillcolor="orange")
#t.begin_fill()
#t.circle(90)
#t.end_fill()

#Zone Gauche
turtle.goto(-240,120)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-211,97)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-211,-17)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-240,-40)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#Zone Droite
turtle.goto(240,120)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(211,97)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(211,-17)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(240,-40)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#Large
turtle.goto(-166,180)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-108.8,120)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(108.8,120)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(166,180)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-80,40)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(80,40)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-48,-40)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(48,-40)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#Gobi Rochers
turtle.goto(-99,-191)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-87,-131)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-33,-131)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(-21,-191)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(21,-191)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(33,-131)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(87,-131)
turtle.pen(pencolor="red", fillcolor="red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.goto(99,-191)
turtle.pen(pencolor="green", fillcolor="green")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.home()

###############################################################


turtle.mainloop()
