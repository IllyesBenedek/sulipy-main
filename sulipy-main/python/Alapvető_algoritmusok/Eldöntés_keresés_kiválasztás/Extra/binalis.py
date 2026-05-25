# Bináris keresés – rendezett listában keres

lista = [2, 5, 8, 12, 16, 23, 28, 32, 37, 41, 45, 52, 58, 63, 71, 78, 85]

keresett = int(input("Adj meg egy számot: "))

also = 0
felso = len(lista) - 1
talalt = False

while also <= felso:
    kozep = (also + felso) // 2
    
    if lista[kozep] == keresett:
        talalt = True
        break
    elif lista[kozep] < keresett:
        also = kozep + 1
    else:
        felso = kozep - 1

if talalt:
    print(keresett, "megtalálva! Indexe:", kozep)
else:
    print(keresett, "nem szerepel a listában!")
