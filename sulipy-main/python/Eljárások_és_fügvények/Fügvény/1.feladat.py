def osszegzo(*args):
    osszeg = 0
    for i in args:
        osszeg += i
    return osszeg


print(osszegzo(1, 2, 3, 4, 5))
