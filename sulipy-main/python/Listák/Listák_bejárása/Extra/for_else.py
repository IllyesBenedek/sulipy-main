szavak = ["asztal", "lámpa", "ablak", "kutya", "alma", "kukta"]
talalat = False

for szo in szavak:
    if szo[0] == "a" and szo[-1] == "a":
        talalat = True
        print("Van ilyen szó!")
        break
else:
    print("Nincs ilyen szó!")
