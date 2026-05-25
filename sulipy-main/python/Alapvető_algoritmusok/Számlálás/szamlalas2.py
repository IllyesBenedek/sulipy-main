szavak = ["Elemér", "tó", "ajtó", "róka", "egér", "Aladár", "pingvin"]

darab = 0
for szo in szavak:
    if len(szo) > 4:
        darab += 1
print("A listában 4-nél több betüböl álló szavak száma:", darab)
