import random

oszlopok = ["A", "B", "C"]
sorok = ["1", "2", "3"]

hajó = random.choice(oszlopok) + random.choice(sorok)

probalkozas = 0

print("Torpedó játék! Találd el a hajó pozícióját! (pl: A1)")

tipp = input("Add meg a pozíciót: ")

while tipp != hajó:
    probalkozas += 1
    print("Nem találtad el!")
    tipp = input("Add meg a pozíciót: ")

probalkozas += 1
print("Eltaláltad! A hajó pozíciója:", hajó)
print("Próbálkozások száma:", probalkozas)
