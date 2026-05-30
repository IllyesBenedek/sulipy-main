import random

szam = random.randint(1, 10)
print(szam)

szinek = ["piros", "kék", "zöld"]
szin = random.choice(szinek)
print(szin)

szamok = [1, 2, 3, 4, 5]
random.shuffle(szamok)
print(szamok)

tort = random.random()
print(tort)
