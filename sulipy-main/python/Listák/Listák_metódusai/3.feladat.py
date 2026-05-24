betuk = []

betu = input("Adj meg egy betűt (ENTER a véghez): ")

while betu != "":
    if betu.lower() in [b.lower() for b in betuk]:
        print("Ezt a betűt már rögzítettem.")
    else:
        betuk.append(betu)

    betuk.sort()
    print("Rögzített betűk:", ", ".join(betuk))

    betu = input("Adj meg egy betűt (ENTER a véghez): ")
