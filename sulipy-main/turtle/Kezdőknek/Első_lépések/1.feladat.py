import turtle

turtle.pen(fillcolor="yellow", pencolor="blue", pensize=3)
turtle.shape("turtle")

turtle.begin_fill()
for i in range(5):
    turtle.forward(150)
    turtle.left(72)
turtle.end_fill()

turtle.done()
