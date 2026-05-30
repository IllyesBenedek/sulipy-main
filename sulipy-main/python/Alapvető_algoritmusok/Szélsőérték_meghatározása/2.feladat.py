szavak = []

szo = input("Adj meg egy szót (ENTER a véghez): ")

while szo != "":
    szavak.append(szo)
    szo = input("Adj meg egy szót (ENTER a véghez): ")

if szavak != []:
    legrovidebb = szavak[0]
    leghosszabb = szavak[0]
    for i in szavak:
        if len(i) < len(legrovidebb):
            legrovidebb = i

        if len(i) > len(leghosszabb):
            leghosszabb = i

    print("Lista:", szavak)
    print("Legrövidebb:", legrovidebb)
    print("Leghosszabb:", leghosszabb)
else:
    print("Nem adtál meg szót!")
