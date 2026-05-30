szamok = []

szam = input("Adj meg egy számot (x a véghez): ")

while szam != "x" and szam != "x":
    szamok.append(int(szam))
    szam = input("Adj meg egy számot (x a véghez): ")

parosok = []
for i in szamok:
    if i % 2 == 0:
        parosok.append(i)

if parosok != []:
    min = parosok[0]
    max = parosok[0]
    for i in parosok:
        if i < min:
            min = i
        if i > max:
            max = i
    print("Lista:", szamok)
    print("Legkisebb páros:", min)
    print("Legnagyobb páros:", max)
else:
    print("Nincs páros szám a listában!")
