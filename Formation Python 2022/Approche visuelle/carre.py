import turtle

t = turtle.Turtle()

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


def tracer_carres(taille_depart, nb):
    for i in range(0, nb):
        taille = (i+1)*(i+1)*taille_depart
        carre(taille)

tracer_carres(8, 6)
turtle.done()