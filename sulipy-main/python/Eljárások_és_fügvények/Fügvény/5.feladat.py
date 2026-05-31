def legkisebb(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min


szamok = []

szam = int(input("Adj meg egy számot (negatív a véghez): "))

while szam >= 0:
    szamok.append(szam)
    szam = int(input("Adj meg egy számot (negatív a véghez): "))

if szamok != []:
    print("A legkisebb szám:", legkisebb(szamok))
else:
    print("Nem adtál meg számot!")
