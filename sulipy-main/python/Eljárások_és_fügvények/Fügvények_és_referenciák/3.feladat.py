import random


def betut_ker():
    return input("Adj meg egy betűt! ")


def allapot(szo, talalatok):
    eredmeny = ""
    for betu in szo:
        if betu in talalatok:
            eredmeny += betu
        else:
            eredmeny += "_"
    return eredmeny


def main():
    szavak = ["tábla", "szék", "ablak", "könyv", "ceruza"]
    szo = random.choice(szavak)

    talalatok = []
    rossz_tippek = []
    probalkozas = 0

    print("Találd ki, melyik ötbetűs főnévre gondoltam!")

    while allapot(szo, talalatok) != szo:
        betu = betut_ker()
        probalkozas += 1

        if betu in szo:
            print("Találat!")
            if betu not in talalatok:
                talalatok.append(betu)
        else:
            print("Sajnos nem talált!")
            if betu not in rossz_tippek:
                rossz_tippek.append(betu)

        print(f"Jelenlegi állás: {allapot(szo, talalatok)}")
        print(f"Rossz tippek: {', '.join(rossz_tippek)}")
        print("------------------------------------------")

    print(f"Gratulálok! Kitaláltad {probalkozas} próbálkozásból!")


main()
