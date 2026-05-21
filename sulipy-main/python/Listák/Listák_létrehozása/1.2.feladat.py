nevek = []

nev = input("Adj meg egy keresztnevet (vagy ENTER a véghez): ")

while nev != "" and len(nevek) < 3:
    nevek.append(nev)
    if len(nevek) == 3:
        print("Már nincs lehetőséged újabb adat bevitelére!")
    else:
        nev = input("Adj meg egy keresztnevet (vagy ENTER a véghez): ")

print("A bekért nevek:")
print(nevek)
