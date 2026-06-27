import turtle

turtle.pen(fillcolor="lightblue", pencolor="black", pensize=2)

# 1. téglalap
turtle.begin_fill()
for _ in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()

# 2. téglalap
turtle.forward(150)

turtle.begin_fill()
for _ in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()

turtle.done()
