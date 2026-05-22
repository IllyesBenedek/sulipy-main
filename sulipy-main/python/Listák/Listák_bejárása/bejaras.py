tantargyak = ["matek", "töri", "biologia", "kémia", "informatika"]

index = 0
for tantargy in tantargyak:
    print(index, tantargy)
    index += 1

for index in range(len(tantargyak)):
    print(index, tantargyak[index])

for index, tantargy in enumerate(tantargyak):
    print(index, tantargy)

# Mind a 3 ugyan azt csinálja!
