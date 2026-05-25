szamok = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while index < len(szamok) and not talalat:
    if szamok[index] % 3 == 0:
        talalat = True
    index += 1

if talalat:
    print("Van a listában hárommal osztható szám, az indexe:", index-1)
else:
    print("Nincs a listában hárommal osztható szám.")
