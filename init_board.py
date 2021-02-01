import turtle
from random import randint
gr = "green"
rd = "red"
ble = "blue"
yl = "yellow"

def dessinCercle(x,y,color):
    turtle.goto(x,y)
    turtle.pen(pencolor=color, fillcolor=color)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

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

#Gobi sideblue base
dessinCercle(-240,120,rd)
dessinCercle(-211,97,gr)
dessinCercle(-211,-17,rd)
dessinCercle(-240,-40,gr)
#Gobi sideyellow base
dessinCercle(240,120,gr)
dessinCercle(211,97,rd)
dessinCercle(211,-17,gr)
dessinCercle(240,-40,rd)
#Gobi sideblue large
dessinCercle(-166,180,rd)
dessinCercle(-108.8,120,gr)
dessinCercle(-80,40,rd)
dessinCercle(-48,-40,gr)
#Gobi sideyellow large
dessinCercle(166,180,gr)
dessinCercle(108.8,120,rd)
dessinCercle(80,40,gr)
dessinCercle(48,-40,rd)
#Gobi Rochers sideyellow
dessinCercle(-99,-191,rd)
dessinCercle(-87,-131,gr)
dessinCercle(-33,-131,rd)
dessinCercle(-21,-191,gr)
#Gobi Rochers sideblue
dessinCercle(21,-191,rd)
dessinCercle(33,-131,gr)
dessinCercle(87,-131,rd)
dessinCercle(99,-191,gr)
###############################################################
turtle.home()
turtle.mainloop()
