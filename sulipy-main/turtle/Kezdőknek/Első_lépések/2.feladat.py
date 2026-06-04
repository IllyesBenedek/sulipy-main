import turtle

turtle.shape("turtle")
turtle.pensize(3)

for oldal in range(4):
    for i in range(10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    turtle.left(90)

turtle.done()
