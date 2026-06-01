import random


def bekero():
    return int(input("Adj meg egy számot (0 a véghez): "))


def main():
    szam = random.randint(1, 10)
    print(f"Generált szám: {szam=}")

    be = bekero()

    while be != 0:
        szam = be
        print(f"Felülírt szám: {szam=}")
        be = bekero()

    print(f"Végső szám: {szam=}")
    print("Vége!")


main()
