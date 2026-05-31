def harommal_oszthatok(lista):
    darab = 0
    for i in lista:
        if i % 3 == 0:
            darab += 1
    return darab


szamok = []

szam = int(input("Adj meg egy számot (negatív a véghez): "))

while szam >= 0:
    szamok.append(szam)
    szam = int(input("Adj meg egy számot (negatív a véghez): "))

print("Lista:", szamok)
print("Hárommal osztható számok darabszáma:", harommal_oszthatok(szamok))
