szamok = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while not talalat:
    if szamok[index] % 3 == 0:
        talalat = True
    index += 1

print("Van a listában hárommal osztható szám indexe:", index-1)
