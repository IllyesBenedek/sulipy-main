szam = int(input("Adj meg egy egész számot:"))

if szam > 0 and szam % 2 == 0:
    print("A szám pozitív és páros! ")
elif szam < 0 and szam % 2 != 0:
    print("A szám negatív és páratlan! ")
else:
    print("A szám nem pozitív páros és nem negatív páratlan! ")