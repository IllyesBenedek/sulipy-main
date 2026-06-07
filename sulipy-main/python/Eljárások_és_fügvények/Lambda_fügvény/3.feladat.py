szavak = ['alma', 'ló', 'padló', 'citrom', 'kávé', 'nyugalom']

eredmeny1 = list(filter(lambda szo: 'l' in szo, szavak))
print(eredmeny1)

eredmeny2 = [szo for szo in szavak if 'l' in szo]
print(eredmeny2)
