szam_1 = 250
szam_2 = 500
szamok = [3, 2, 1]

print(f"{szam_1} | {type(szam_1)} | {id(szam_1)}")
print(f'{szam_2=} | {type(szam_2)} | {id(szam_2)}')
print(f'{szamok=} | {type(szamok)} | {id(szamok)}')

print(szam_1.__abs__())
szamok.sort()
print(szamok)
