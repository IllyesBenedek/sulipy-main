def b_oldal(teglalap):
    return teglalap[1]


teglalapok = [[1, 9], [2, 3], [5, 7]]

print(max(teglalapok, key=b_oldal))
print(max(teglalapok, key=lambda teglalap: teglalap[1]))
print(min(teglalapok, key=lambda teglalap: teglalap[0] * teglalap[1]))

# lambda függvény:
# névtelen, kis függvény
# tetszőleges számú argumentum
# egyetlen egy kifejezés visszatérési értékként

koszont = lambda vezeteknev, keresztnev: f"szia {vezeteknev} {keresztnev}!"
print(koszont("Kis", "Peter"))
