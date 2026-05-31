def harommal_oszthatok(szam):
    harom = 0
    for i in szam:
        if i % 3 == 0:
            harom += 1
    return harom


print(harommal_oszthatok([1, 3, 6, 7, 9, 11, 12]))
