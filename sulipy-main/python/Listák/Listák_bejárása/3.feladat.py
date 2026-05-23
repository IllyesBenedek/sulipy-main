szamok = [12, 7, 3, 18, 5, 24, 9, 36, 11, 6, 15, 42]

eredmeny = []

for szam in szamok:
    if szam % 3 == 0 and szam % 2 == 0:
        eredmeny.append(szam)
print(eredmeny)
