
lista = [2, 5, 4, 8, 9, 11, 10, 12]

for szam in lista:
    if szam % 3 == 0:
        print('Van a listában hárommal osztható szám.')
        break
else:
    print('Nincs a listában hárommal osztható szám.')
