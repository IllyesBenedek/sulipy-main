szavak = ["alma", "körte", "Árvíz", "Alma", "ananász", "eper", "Egres"]

darab = 0
a_szavak = []

for i in szavak:
    if i[0] == "a" or i[0] == "A":
        darab += 1
        a_szavak.append(i)

print("Darabszám:", darab)
print("A szavak:", a_szavak)
