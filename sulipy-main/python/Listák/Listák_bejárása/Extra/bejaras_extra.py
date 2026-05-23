szamok = [1, 7, 8, 10, 12, 9, 3]

for szam in szamok:
    if szam % 2 == 0:
        print('Megvan az első páros szám a listában:')
        print(szam)
        break             # megszakítja a lista bejárását
print('Program vége')
