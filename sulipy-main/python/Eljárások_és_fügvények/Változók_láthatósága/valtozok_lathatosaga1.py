# Global (function) scope

def negyzet(a):
    print(f"A negyzet függvényen belül: {a}")
    return a ** 2


def kob(a):
    print(f"A kob függvényen belül: {a}")
    return a ** 2


a = 0
print(f"A függvényen kivül: {a}")
print(negyzet(2))
print(kob(3))
