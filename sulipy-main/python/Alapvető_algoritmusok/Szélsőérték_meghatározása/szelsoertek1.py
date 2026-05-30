szavak = ["Elemér", "tó", "ajtó", "róka", "egér", "Aladár", "pingvin"]

legrovidebb = szavak[0]
for szo in szavak:
    if len(szo) < len(legrovidebb):
        legrovidebb = szo

print("A lista legrövidebb szava: ", legrovidebb)
