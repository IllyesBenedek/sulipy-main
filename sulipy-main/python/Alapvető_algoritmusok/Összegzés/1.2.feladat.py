import random

szamok = [random.randint(1, 10) for i in range(5)]

osszeg = 0
for i in szamok:
    if i % 2 == 0:
        osszeg += i

print(szamok)
print("Páros számok összege:", osszeg)
