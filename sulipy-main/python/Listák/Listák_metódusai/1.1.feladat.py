szinek = ["piros", "kék", "zöld", "sárga", "fehér", "fekete"]

szin = input("Adj meg egy színt: ")

if szin in szinek:
    print("A", szin, "szín szerepel a listában!")
else:
    print("A", szin, "szín nem szerepel a listában!")

print(", ".join(szinek))
