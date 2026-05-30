def szam_vizsgalat(szam):
    if szam < 0:
        print(str(szam) + "negatív")
    elif szam > 0:
        print(str(szam) + " pozitív")
    else:
        print("A szám nulla")


szam_vizsgalat(-5)
szam_vizsgalat(3)
szam_vizsgalat(0)
