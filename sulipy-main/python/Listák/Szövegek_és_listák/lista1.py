lista = [1, 2, 3, 4, 5, 6, 7]
string = "jöttem, láttam, győztem!"

for elem in lista:
    print(elem)

szamlalo = 0
for karakter in string:
    if karakter == "a" or karakter == "á":
        szamlalo += 1
print(szamlalo)
