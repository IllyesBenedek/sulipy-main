szinek = ["piros", "kék", "zöld", "sárga", "fehér", "fekete", "piros", "kék"]

szin = input("Adj meg egy színt: ")

if szin in szinek:
    print("A", szin, "szín", szinek.count(szin), "alkalomal szerepel listában")
else:
    print("A megadott szín nem szerepel a listában.")

print(", ".join(szinek))
