"""
Hőmérséklet értékek 7:00, 15:00, 23:00 órakor
"""
homersekletek = [[11, 19, 17], [13, 22, 20], [15, 30, 25], [7, 16, 15]]
print(homersekletek[0])
for nap in homersekletek:
    for meres in nap:
        print(meres)
    print("------")
