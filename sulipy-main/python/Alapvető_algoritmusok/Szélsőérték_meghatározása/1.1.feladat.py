szamok = []

szam = input("Adj meg egy számot (ENTER a véghez): ")

while szam != "":
    szamok.append(int(szam))
    szam = input("Adj meg egy számot (ENTER a véghez): ")

if szamok != []:
    min = szamok[0]
    max = szamok[0]
    for szam in szamok:
        if szam < min:
            min = szam
        if szam > max:
            max = szam
    print("Lista:", szamok)
    print("Legkisebb:", min)
    print("Legnagyobb:", max)
else:
    print("Nem adtál meg számot!")
