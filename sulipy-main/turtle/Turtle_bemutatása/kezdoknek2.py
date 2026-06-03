import turtle
import time

szin = "blue"
sebesseg = 5
turtle.shape("turtle")
turtle.pen(fillcolor="red", pencolor=szin, pensize=20)
turtle.speed(sebesseg)
turtle.seth(45)

turtle.begin_fill()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.goto(0, 0)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.home()
turtle.end_fill()
time.sleep(2)
turtle.undo()
