def paros_e(parosok):
    for i in parosok:
        if i % 2 == 0:
            return True
    return False


print(paros_e([1, 3, 5, 7]))
print(paros_e([1, 3, 4, 7]))
