nevek = ["Anna", "Tomi", "Béla", "Tamás", "Kata", "Tibor", "Péter", "tanár",]

t_szavak = []

for nev in nevek:
    if nev[0].lower() == "t":
        t_szavak.append(nev)
print(t_szavak)
