# Global (module) scope

def negyzet(a):
    global szam
    szam = 10
    print(f"A negyzet függvényen belül: {szam}")
    return a ** 2


print(negyzet(2))
print(f"A negyzet függvényen kivül: {szam}")
