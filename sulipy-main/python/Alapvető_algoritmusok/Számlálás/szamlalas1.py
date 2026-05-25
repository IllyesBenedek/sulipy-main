szamok = [12, 5, 4, 8, 9, 11, 10, 12, 6]

darab = 0
for szam in szamok:
    if szam % 3 == 0:
        darab += 1
print("A 3-mal osztható számok száma:", darab)
