szam = int(input("Adj meg egy páros számot: "))

while szam % 2 != 0:
    print("Ez páratlan szám! Kérlek adj meg egy páros számot! ")
    szam = int(input("Adj meg egy páros számot: "))

print("Köszönöm", szam, "valóban páros szám! ")
