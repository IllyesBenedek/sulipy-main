szam = int(input("Adj meg egy páros számot! "))

fele = szam // 2

sor = 1

while sor <= fele:
    print("O " * sor)
    sor += 1

sor = fele

while sor >= 1:
    print("O " * sor)
    sor -= 1
