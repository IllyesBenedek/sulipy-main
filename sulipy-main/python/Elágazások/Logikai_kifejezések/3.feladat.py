szam = int(input("Adj meg egy számot: "))

if szam % 3 == 0:
    print("A szám csak 3 mal osztható!")
elif szam % 4 == 0:
    print("A szám csak 4 mal osztható!")
else:
    print("A szám 3-mal se 4-gyel sem osztható!")
