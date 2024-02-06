# Operasi logika atau boolean

#Not
print("=====Not====")
a = True
c = not a
print("data a=", c)

print("\n------------------\n")

#OR (jadi kesimpulannya adalah untuk OR, jika salah satunya ada yang True , maka hasilnya adalah True)
print("=====OR====")
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

print("\n------------------\n")

#AND (Jika 2 buah nilai True, maka hasilnya True)
print("=====AND====")
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

print("\n------------------\n")

#XOR (Akan True bila salah satunya True, sisanya akan False)
print("=====XOR====")
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

print("\n------------------\n")