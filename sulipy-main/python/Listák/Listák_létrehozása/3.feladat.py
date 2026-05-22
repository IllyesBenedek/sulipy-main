import random

szamok = []
szamlalo = 0

while szamlalo < 10:
    szam = random.randint(0, 50)
    if szam % 4 == 0:
        szamok.append(szam)
    szamlalo += 1

print("A 4-gyel osztható számok:", szamok)
print("A lista elemszáma:", len(szamok))
