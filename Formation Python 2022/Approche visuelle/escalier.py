import turtle

t = turtle.Turtle()

def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -=10
    t.forward(30)

escalier(50, 7)
turtle.done()