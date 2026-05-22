a_szavak = []

print("Adj meg 'a' betűvel kezdődő szavakat! (ENTER a véghez)")

szo = input("Adj meg egy szót: ")

while szo != "":
    if szo[0] == "a":
        a_szavak.append(szo)
    else:
        print("Nem 'a' betűvel kezdődik, kihagyjuk!")
    szo = input("Adj meg egy szót: ")

print("A tárolt szavak:", a_szavak)
print("Összesen:", len(a_szavak), "szó.")
