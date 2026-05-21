sor = 0

while sor < 7:
    oszlop = 0
    while oszlop < 7:
        if sor == oszlop or sor + oszlop == 6:
            print("O", end=" ")
        else:
            print(".", end=" ")
        oszlop += 1
    print()
    sor += 1
