import random

gondolt_szam = random.randint(1, 5)

tip = int(input("Adj meg egy számot1 és 5 között! találd ki:  "))

if tip == gondolt_szam:
    print("Gratulálok eltaláltad")
elif tip < gondolt_szam:
    print("A gondolt szám ennél nagyobb")
else:
    print("A gondolt szám ennél kissebb")
