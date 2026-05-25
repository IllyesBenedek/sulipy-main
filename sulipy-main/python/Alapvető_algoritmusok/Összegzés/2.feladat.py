szamok = []
osszeg = 0

szam = int(input("Adj meg egy számot [-5;5]: "))

while -5 <= szam <= 5:
    szamok.append(szam)
    osszeg += szam
    szam = int(input("Adj meg egy számot [-5;5]: "))

print(szamok)
print("Összeg:", osszeg)
