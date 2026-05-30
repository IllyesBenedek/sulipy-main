szamok = [12, 5, 4, 8, 9, 5, -2, 11, 10, 12, 6]

min = szamok[0]

max = szamok[0]
for szam in szamok:
    if szam < min:
        min = szam

    if szam > max:
        max = szam

print("A lista legkisebb eleme: ", min)

print("A lista legnagyobb eleme: ", max)
