import turtle
import constantes
import robot_mouvment
import init_board

turtle.colormode(0xFF)
turtle.speed(100)
turtle.shapesize(0.1, 0.1, 0.1)
turtle.penup()
init_board.dessin_Gobies_init()

def dessin_Gobies_init():
    """
    Dessine l'ensemble des gobies de la table (à ne faire qu'une fois). Dans
    l'état les éléments de la liste sont en unité turtle centré donc on applique
    juste ECHELLE.
    """
    for i in range(0, 24):
        dessin_Cercle(
            LISTEGOBI[i][0]*ECHELLE, LISTEGOBI[i][1]*ECHELLE, LISTEGOBI[i][2]
        )

turtle.mainloop()
