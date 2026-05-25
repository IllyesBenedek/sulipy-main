import random

szamok = [random.randint(1, 10) for i in range(5)]

osszeg = 0
for i in szamok:
    osszeg += i

print(szamok)
print("Összeg:", osszeg)
