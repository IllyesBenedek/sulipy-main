import turtle
import time
import random

colors = ["orange", "black", "red", "yellow", "blue", "green"]

turtle.shape("turtle")
turtle.pen(pencolor=random.choice(colors),
           fillcolor=random.choice(colors),
           pensize=random.randint(0, 10))

turtle.begin_fill()
for _ in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()


time.sleep(5)
