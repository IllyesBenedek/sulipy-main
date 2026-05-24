# eldöntés
szavak = ["lámpa", "ablak", "kutya", "Attila", "kukta"]

for szo in szavak:
    print(szo)
    if szo[0] == "a":
        print("Van a betüvel kezdődő szó!")
        break
else:
    print("Nincs ilyen szó!")
