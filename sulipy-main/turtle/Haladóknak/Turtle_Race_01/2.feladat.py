import turtle
import time

MAX_X, MAX_Y = 400, 250
WIDTH, HEIGHT = MAX_X * 2 + 80, MAX_Y * 2 + 40
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)

cel = turtle.Turtle()
cel.penup()
cel.setpos(MAX_X - 20, MAX_Y)
cel.pen(pencolor="black", pensize=7)
cel.right(90)

dash_length = 20
gap_length = 15
total = MAX_Y * 2
drawn = 0

while drawn < total:
    cel.pendown()
    cel.forward(min(dash_length, total - drawn))
    drawn += dash_length
    cel.penup()
    cel.forward(min(gap_length, total - drawn if drawn < total else 0))
    drawn += gap_length

noris = turtle.Turtle()
noris.shape("turtle")
noris.shapesize(stretch_wid=2, stretch_len=2, outline=4)
noris.pen(pencolor="blue", fillcolor="orange", pensize=9)
noris.penup()
noris.setpos(-MAX_X, 0)
noris.pendown()
noris.forward(MAX_X * 2)

ferstapen = turtle.Turtle()
ferstapen.shape("turtle")
ferstapen.shapesize(stretch_wid=3, stretch_len=3, outline=4)
ferstapen.pen(pencolor="red", fillcolor="green", pensize=9)
ferstapen.penup()
ferstapen.setpos(-MAX_X, -80)
ferstapen.pendown()
ferstapen.forward(MAX_X * 2)

time.sleep(5)
