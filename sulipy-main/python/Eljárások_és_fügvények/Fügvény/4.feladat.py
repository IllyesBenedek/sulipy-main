def kerulet(a, *args):
    if len(args) == 0:
        return 4 * a
    elif len(args) == 1:
        return 2 * (a + args[0])
    elif len(args) == 2:
        return a + args[0] + args[1]
    else:
        osszeg = a
        for i in args:
            osszeg += i
        return osszeg


print("Négyzet kerülete:", kerulet(5))
print("Téglalap kerülete:", kerulet(4, 6))
print("Háromszög kerülete:", kerulet(3, 4, 5))
print("Sokszög kerülete:", kerulet(2, 3, 4, 5, 6))
