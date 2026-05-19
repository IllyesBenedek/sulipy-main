import random

erme = random.randint(1, 2)

valasz = input("Fej vagy írás! ")

if erme == 1:
    gep = "fej"
else:
    gep = "írás"

if valasz == gep:
    print("Gratulálok eltaláltad! A helyes válasz::", gep)
else:
    print("Sajnos nem találtad el! A helyes válsz:", gep)
