import random

szamok = [random.randint(1, 7) for i in range(5)]

szam = int(input("Adj meg egy számot: "))

if szam in szamok:
    print(szam, "szerepel a listában!")
else:
    print(szam, "nem szerepel a listában!")

print(szamok)
