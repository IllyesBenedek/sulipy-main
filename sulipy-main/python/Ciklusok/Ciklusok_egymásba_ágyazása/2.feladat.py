sor = 0

while sor < 5:
    oszlop = 0
    while oszlop < 5:
        if sor == oszlop:
            print("O", end=" ")
        else:
            print(".", end=" ")
        oszlop += 1
    print()
    sor += 1
