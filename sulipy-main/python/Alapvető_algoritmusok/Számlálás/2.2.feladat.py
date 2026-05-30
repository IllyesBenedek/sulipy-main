szavak = ["alma", "körte", "Árvíz", "Alma", "ananász", "eper", "Egres"]

darab = 0
e_szavak = []

for i in szavak:
    if "e" in i or "E" in i:
        darab += 1
        e_szavak.append(i)

print("Darabszám:", darab)
print("E betűt tartalmazó szavak:", e_szavak)
