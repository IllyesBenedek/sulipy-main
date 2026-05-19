henrik = (input("Jön Henrik ma kosarazni (igen/nem): "))
hanna = input("Jön Hanna ma kosarazni (igen/nem): ")

if henrik == "nem" and hanna == "nem":
    print("Egyikük sem jön kosarazni! ")
elif henrik == "igen" and hanna == "igen":
    print("Mind a ketten jönek kosarazni! ")
else:
    print("Csak az egyikük jön kosarazni!")
