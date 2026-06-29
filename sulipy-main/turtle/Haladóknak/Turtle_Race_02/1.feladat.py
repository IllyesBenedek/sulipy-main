import turtle
import time
import random

MAX_X, MAX_Y = 400, 250
WIDTH, HEIGHT = MAX_X * 2 + 80, MAX_Y * 2 + 40
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)

cel = turtle.Turtle()
cel.penup()
cel.setpos(MAX_X - 20, MAX_Y)
cel.pen(pencolor="black", pensize=1)

negyzet_meret = 20
oszlop_szam = 3
sor_szam = (MAX_Y * 2) // negyzet_meret

for sor in range(sor_szam):
    for oszlop in range(oszlop_szam):
        x = (MAX_X - 20) + oszlop * negyzet_meret
        y = MAX_Y - sor * negyzet_meret
        cel.setpos(x, y)
        if (sor + oszlop) % 2 == 0:
            cel.fillcolor("black")
        else:
            cel.fillcolor("white")
        cel.begin_fill()
        cel.pendown()
        for _ in range(4):
            cel.forward(negyzet_meret)
            cel.right(90)
        cel.end_fill()
        cel.penup()


noris = turtle.Turtle()
noris.shape("turtle")
noris.shapesize(stretch_wid=2, stretch_len=2, outline=4)
noris.pen(pencolor="blue", fillcolor="orange", pensize=9)
noris.penup()
noris.setpos(-MAX_X, 0)
noris.pendown()
# noris.forward(MAX_X * 2)
futam = True
while futam:
    r = random.randint(1, 10)
    noris.pensize(r)
    noris.forward(r * 2)
    x, y = noris.pos()
    if x >= MAX_X - 20:
        futam = False

time.sleep(5)
