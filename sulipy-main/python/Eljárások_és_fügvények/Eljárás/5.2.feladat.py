def mezot_rajzol(sor, oszlop):
    for i in range(3):
        for j in range(6):
            if i == sor and j == oszlop:
                print("+", end=" ")
            else:
                print("O", end=" ")
        print()


while True:
    sor = int(input("Add meg a sort (0-2): "))
    if sor < 0:
        break
    oszlop = int(input("Add meg az oszlopot (0-5): "))
    if oszlop < 0:
        break
    if sor > 2 or oszlop > 5:
        print("Érvénytelen koordináta!")
    else:
        mezot_rajzol(sor, oszlop)
