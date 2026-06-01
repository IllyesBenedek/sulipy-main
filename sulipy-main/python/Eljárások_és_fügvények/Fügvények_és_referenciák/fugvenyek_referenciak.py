# Vizsgálat int tipussal
def fgv_1(x):
    x += 1


szam = 300
print(f'Függvényhívás előtt: {szam=}')
fgv_1(szam)
print(f'Függvényhívás után: {szam=}')


# Vizsgálat int tipussal
def fgv_2(x):
    x[0] += 17


szamok = [1, 2, 3, 4]
print(f'Függvényhívás előtt: {szamok=}')
fgv_2(szamok)
print(f'Függvényhívás után: {szamok=}')
