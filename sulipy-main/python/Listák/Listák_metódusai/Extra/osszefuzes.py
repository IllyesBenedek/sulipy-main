diakok = ["Nora", "Gergo", "Hanna", "Tamas", "Adam"]
eletkorok = [17, 16, 18, 18, 15]

for index in range(len(diakok)):
    print(f"{diakok[index]}: {eletkorok[index]}")

for diak, eletkor in zip(diakok, eletkorok):
    print(f"{diak}: {eletkor}")

print(list(zip(diakok, eletkorok)))
