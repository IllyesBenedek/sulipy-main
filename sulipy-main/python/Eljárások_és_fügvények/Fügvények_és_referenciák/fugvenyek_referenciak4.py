def teglalapot_novel(a, b):
    a *= 2
    b *= 2
    return a, b


a_oldal = 3
b_oldal = 9
a_oldal, b_oldal = teglalapot_novel(a_oldal, b_oldal)

print(a_oldal, b_oldal)
