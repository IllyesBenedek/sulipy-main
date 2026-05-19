import random

a = random.randint(0, 10)
b = random.randint(0, 10)
print(f"Itt van két szám {a} és {b}, milyen műveletett végezük velük?")
valasz = input(f"Add meg a műveleti jelet! ")

match valasz:
    case "+":
        print(f"{a} {valasz} {b} = {a + b}")
    case "-":
        print(f"{a} {valasz} {b} = {a - b}")
    case "*":
        print(f"{a} {valasz} {b} = {a * b}")
    case  "/" if b != 0:
        print(f"{a} {valasz} {b} = {a * b}")
    case  "**" | "%":
        print("Ezt a műveletet még nem ismerem!")
    case other:
        #   case_:
        print("?!!")
