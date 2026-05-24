# kivalogatás
szavak = ["lámpa", "ablak", "kutya", "Attila", "kukta"]

for szo in szavak:
    if szo[0] == "a":
        continue
    print(szo)

for szo in szavak:
    if szo != "a":
        print(szo)
