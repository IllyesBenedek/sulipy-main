import random

szamok = [random.randint(1, 10) for i in range(5)]

darab = 0
for i in szamok:
    if i % 2 == 0:
        darab += 1

print(szamok)
print("A páros számok darabszáma:", darab)
