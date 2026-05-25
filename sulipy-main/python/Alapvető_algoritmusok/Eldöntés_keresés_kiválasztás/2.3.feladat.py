szo = "python"

jo_tippek = []
rossz_tippek = []

betu = input("Adj meg egy betűt (ENTER a véghez): ")

while betu != "":
    if betu in szo:
        print("Igen,", betu, "szerepel a szóban!")
        if betu not in jo_tippek:
            jo_tippek.append(betu)
    else:
        print("Nem,", betu, "nem szerepel a szóban!")
        if betu not in rossz_tippek:
            rossz_tippek.append(betu)

    print("Jó tippek:", jo_tippek)
    print("Rossz tippek:", rossz_tippek)

    betu = input("Adj meg egy betűt (ENTER a véghez): ")
