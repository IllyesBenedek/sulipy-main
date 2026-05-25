szam = int(input("Adj meg egy nemnegatív egész számot: "))

if szam < 0:
    print("Negatív számnak nincs faktoriálisa!")
else:
    fakto = 1
    for i in range(1, szam + 1):
        fakto *= i
    print(szam, "faktoriálisa:", fakto)
