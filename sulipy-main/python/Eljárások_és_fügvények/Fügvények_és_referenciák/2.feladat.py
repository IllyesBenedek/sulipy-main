def bekero():
    a = input("Adj meg egy betűt: ")
    b = input("Adj meg egy betűt: ")
    c = input("Adj meg egy betűt: ")
    return [a, b, c]


def harom_egyforma(lista):
    return lista[0] == lista[1] == lista[2]


def main():
    lista = ["a", "b", "c"]
    print(f"{lista=}")

    lista = bekero()

    while not harom_egyforma(lista):
        print(f"{lista=}")
        lista = bekero()

    print(f"{lista=}")
    print("Három egyforma betű! Vége!")


main()
