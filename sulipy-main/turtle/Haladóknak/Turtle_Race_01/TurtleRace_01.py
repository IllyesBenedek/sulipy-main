import turtle
import time

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
cel.forward(MAX_Y * 2)

noris = turtle.Turtle()
noris.shape("turtle")
noris.shapesize(stretch_wid=2, stretch_len=2, outline=4)
noris.pen(pencolor="blue", fillcolor="orange", pensize=9)
noris.penup()
noris.setpos(-MAX_X, 0)
noris.pendown()
noris.forward(MAX_X * 2)

time.sleep(5)
