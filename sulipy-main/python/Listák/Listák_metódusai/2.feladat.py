import random

szamok = []

for i in range(10):
    szamok.append(random.randint(1, 3))

print("A generált lista:", szamok)

torlendo = int(input("Adj meg egy számot (1-3): "))

while torlendo in szamok:
    szamok.remove(torlendo)

print("A módosított lista:", szamok)
