import random


def eltalalta(tipp, kitalalando):
    return tipp == kitalalando


def tipp_bekero():
    return int(input("Tippelj! "))


def main():
    kitalalando = random.randint(1, 10)
    probalkozas = 0

    print("Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni!")

    tipp = tipp_bekero()
    probalkozas += 1

    while not eltalalta(tipp, kitalalando):
        print(f"Nem találtad el. Ez volt a {probalkozas}. próbálkozásod.")
        tipp = tipp_bekero()
        probalkozas += 1

    print(f"Gratulálok eltaláltad {probalkozas} próbálkozásból!")
    print("Játék vége!")


main()
