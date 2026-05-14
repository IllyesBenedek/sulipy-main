import random

szam = random.randint(-5, 5)
print(szam)

if szam > 0:
    print("A szám pozitív")
elif szam < 0:
    print("A szám negatív")
else:
    print("A megadott szám nulla")
