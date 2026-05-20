import random

darab = 0
szamlalo = 0

while szamlalo <= 20:
    szam = random.randint(1, 12)

    if szam % 3 == 0:
        print(szam)
        darab += 1

        szamlalo += 1

print("A 3-mal osztható számok darabszáma:", darab)
