folytatja = True

while folytatja:
    print("Vidd ki a szemetet")
    valasz = input("Mondjam még egyser? (i/n)")
    if valasz == "n":
        folytatja = False
print("Program vége!")
