szavak = ["lámpa", "ablak", "kutya", "Attila", "kukta"]

index = 0
while index < len(szavak):
    print(szavak[index])
    if szavak[index][0] == "a":
        print("Van a betüvel kezdődő szó!")
        break
    index += 1
else:
    print("Nincs ilyen szó!")
