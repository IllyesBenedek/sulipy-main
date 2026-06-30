import turtle
import time
import random

pilotak_szama = None
while pilotak_szama is None:
    try:
        szam = int(input("Hány pilóta induljon? (1-5) "))
        if 1 <= szam <= 5:
            pilotak_szama = szam
        else:
            print("Csak 1 és 5 közötti számot adj meg!")
    except ValueError:
        print("Számot adj meg!")

MAX_X, MAX_Y = 400, 250
WIDTH, HEIGHT = MAX_X * 2 + 80, MAX_Y * 2 + 40
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)

# Kezdőképernyő és visszaszámlálás
iro = turtle.Turtle()
iro.hideturtle()
iro.pen(pencolor="green", pensize=9)
iro.penup()
iro.goto(-MAX_X + 170, -30)
iro.pendown()
iro.write("Turtle Race", font=("Comic Sans MS", 60, "normal"))
time.sleep(2)
iro.clear()
iro.penup()
iro.goto(-50, -50)
iro.pendown()
for szam in range(3, -1, -1):
    iro.write(str(szam), font=("Comic Sans MS", 100, "normal"))
    time.sleep(1)
    iro.clear()

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
                  ["leclerc", "red", "grey"],
                  ["ocon", "blue", "black"]]

pilotak = []
for _ in range(pilotak_szama):
    pilotak.append(turtle.Turtle())

for index, pilota in enumerate(pilotak):
    pilota.shape("turtle")
    pilota.shapesize(stretch_wid=2, stretch_len=2, outline=4)
    pilota.pen(pencolor=pilotak_adatai[index][1],
               fillcolor=pilotak_adatai[index][2], pensize=9)
    pilota.penup()
    pilota.setpos(-MAX_X, -200 + index * 100)
    pilota.pendown()

    # Piloták neveinek kiírása
    iro.penup()
    iro.goto(-MAX_X, -200 + index * 100 - 40)
    iro.pendown()
    iro.write(pilotak_adatai[index][0], font=("Comic Sans MS", 10, "normal"))

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
