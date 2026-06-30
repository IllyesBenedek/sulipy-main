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
for _ in range(10):
    cel.forward(30)
    cel.penup()
    cel.forward(20)
    cel.pendown()


pilotak_adatai = [["noris", "blue", "orange"],
                  ["ferstapen", "red", "grey"],
                  ["hamilton", "yellow", "green"],
                  ["leclerc", "black", "red"],
                  ["russel", "white", "blue"]]

pilotak = []
for _ in range(3):
    pilotak.append(turtle.Turtle())

for index, pilota in enumerate(pilotak):
    pilota.shape("turtle")
    pilota.shapesize(stretch_wid=2, stretch_len=2, outline=4)
    pilota.pen(pencolor=pilotak_adatai[index][1],
               fillcolor=pilotak_adatai[index][2], pensize=9)
    pilota.penup()
    pilota.setpos(-MAX_X, -100 + index * 100)
    pilota.pendown()

futam = True
while futam:
    for pilota in pilotak:
        r = random.randint(1, 10)
        pilota.pensize(r)
        x, y = pilota.pos()
        pilota.forward(r * 2)
        if x >= MAX_X - 20:
            futam = False
            break

time.sleep(5)
