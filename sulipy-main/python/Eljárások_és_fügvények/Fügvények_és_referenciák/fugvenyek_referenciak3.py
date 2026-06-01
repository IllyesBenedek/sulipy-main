a = 1234567
b = 1234567

print(id(a))
print(id(b))

a += 1
print(id(a))
# Megváltoztatható objektum

c = [1, 2, 3, 4]
d = [1, 2, 3, 4]

print(id(c))
print(id(d))

c.append(17)
print(id(c))
# Megváltoztatatlan objektum

e = "szo"
f = "szo"

print(id(e))
print(id(f))
