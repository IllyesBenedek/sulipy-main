print("Ez a programkiszámolja az átlagodat.")
print("Ha már nem akarsz több jegyet megadni, írj 0-át!")
print("---------------------------------------------")

darab = 0
osszeg = 0

erdemjegy = int(input("Add meg az első jegyet! "))
while erdemjegy != 0:
    darab += 1
    osszeg += erdemjegy
    erdemjegy = int(input("Add meg az következő jegyet! "))

if darab != 0:
    print("A meegadott jegyek átlaga:", osszeg / darab)
else:
    print("Nem adtál meg érdemjegyet!")
