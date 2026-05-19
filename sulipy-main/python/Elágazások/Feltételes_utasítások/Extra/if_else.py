import random

a = random.randint(0, 10)
b = random.randint(0, 10)
print(f"Itt van két szám {a} és {b}, milyen műveletett végezük velük?")
valasz = input(f"Add meg a műveleti jelet! ")

if valasz == "+":
    print(f"{a} {valasz} {b} = {a + b}")
elif valasz == "-":
    print(f"{a} {valasz} {b} = {a - b}")
elif valasz == "*":
    print(f"{a} {valasz} {b} = {a * b}")
elif valasz == "/" and b != 0:
    print(f"{a} {valasz} {b} = {a * b}")
elif "**" or "%":
    print("Ezt a műveletet még nem ismerem!")
else:
    print("?!")
