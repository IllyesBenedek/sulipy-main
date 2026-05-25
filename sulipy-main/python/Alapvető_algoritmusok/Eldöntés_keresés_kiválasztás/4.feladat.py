szoveg = input("Adj meg egy szöveget: ")

maganhangzok = ["a", "e", "i", "o", "u"]

for maganhangzo in maganhangzok:
    helyek = []
    for i in range(len(szoveg)):
        if szoveg[i] == maganhangzo:
            helyek.append(i + 1)

    if len(helyek) > 0:
        print(maganhangzo, "- darabszám:", len(helyek), "- helyek:", helyek)
    else:
        print(maganhangzo, "- nem szerepel a szövegben")
