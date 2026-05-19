import random

gondolt_szam = random.randint(1, 3)

tip = int(input("Gondoltam egy számra 1 és 3 között! találd ki:"))

if tip == gondolt_szam:
    print("Gratulálok eltaláltad!")
elif tip < gondolt_szam:
    print("A gondolt szám ennél nagyobb!")
else:
    print("A gondolt szám ennél kisebb!")
