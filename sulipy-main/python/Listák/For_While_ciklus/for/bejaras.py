szavak = ["lámpa", "ablak", "kutya", "Attila", "kukta"]

for szo in szavak:
    print(szo)

for karakter in "almafa":
    print(karakter)

for index, karakter in enumerate("almafa"):
    print(f"{index}. {karakter}")

for sorszam, karakter in enumerate("almafa", start=1):
    print(f"{sorszam}. {karakter}")

for _ in range(5):
    print("alma")
