def legrojvidebb_szo(lista):
    legrojvidebb = lista[0]
    for szo in lista:
        if len(szo) < len(legrojvidebb):
            legrojvidebb = szo
    print("A legrövidebb szó: " + legrojvidebb)


szavak = []
szavak.append(input("1. szó: "))
szavak.append(input("2. szó: "))
szavak.append(input("3. szó: "))
legrojvidebb_szo(szavak)
