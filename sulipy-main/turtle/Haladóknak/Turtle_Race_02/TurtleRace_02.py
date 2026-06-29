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
cel.pendown()
cel.pen(pencolor="black", pensize=7)
cel.right(90)
# cel.forward(MAX_Y * 2)
for _ in range(10):
    cel.forward(30)
    cel.penup()
    cel.forward(20)
    cel.pendown()


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
