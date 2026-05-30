def mezot_rajzol(sor, oszlop):
    for i in range(3):
        for j in range(6):
            if i == sor and j == oszlop:
                print("+", end=" ")
            else:
                print("O", end=" ")
        print()


mezot_rajzol(0, 4)
