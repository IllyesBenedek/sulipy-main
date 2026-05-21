nevek = []

nev = input("Adj meg egy keresztnevet (vagy ENTER a véghez): ")

while nev != "":
    nevek.append(nev)
    nev = input("Adj meg egy keresztnevet (vagy ENTER a véghez): ")

print("A bekért nevek:")
print(nevek)
