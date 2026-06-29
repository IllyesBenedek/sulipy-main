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

max_ver_stappen = turtle.Turtle()
max_ver_stappen.shape("turtle")
max_ver_stappen.shapesize(stretch_wid=2, stretch_len=2, outline=4)
max_ver_stappen.pen(pencolor="red", fillcolor="blue", pensize=9)
max_ver_stappen.penup()
max_ver_stappen.setpos(-MAX_X, -50)
max_ver_stappen.pendown()

lewis_hamilton = turtle.Turtle()
lewis_hamilton.shape("turtle")
lewis_hamilton.shapesize(stretch_wid=2, stretch_len=2, outline=4)
lewis_hamilton.pen(pencolor="black", fillcolor="silver", pensize=9)
lewis_hamilton.penup()
lewis_hamilton.setpos(-MAX_X, -100)
lewis_hamilton.pendown()

futam = True
gyoztes = ""
nevek = {noris: "Noris",
         max_ver_stappen: "Max Verstappen",
         lewis_hamilton: "Lewis Hamilton"}
while futam:
    for versenyzo in [noris, max_ver_stappen, lewis_hamilton]:
        r = random.randint(1, 10)
        versenyzo.pensize(r)
        versenyzo.forward(r * 2)
        x, y = versenyzo.pos()
        if x >= MAX_X - 20:
            gyoztes = nevek[versenyzo]
            futam = False
            break
        if versenyzo == noris:
            gyoztes = "Noris"
        elif versenyzo == max_ver_stappen:
            gyoztes = "Max Verstappen"
        else:
            gyoztes = "Lewis Hamilton"

print("Győztes:", gyoztes)
screen.title("Győztes: " + gyoztes)

time.sleep(5)
