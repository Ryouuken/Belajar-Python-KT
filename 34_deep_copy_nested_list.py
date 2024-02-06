data0 = [1, 2]
data1 = [3, 4]

data_2D = [data0,data1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data dari nested list
## mengambil data dari list pertama index pertama
data_2D = [0] [0]
print(f"list pertama index pertama {data_2D}")
## mengambil data dari list kedua index pertama
data_2D = [1] [0]
print(f"list kedua index pertama {data_2D}")

# Address semuanya
print(f"Address asli = {hex(id(data_2D))}")
print(f"Address copy = {hex(id(data_2D_copy))}")

### ini harus dimasukin lagi variabelnya karena yang di bagian mengambil data
### si variable data_2D nya jadi berubah, jadinya harus di input ulang, kalau
### tidak si data_2D akan terbaca sebagai integer
data0 = [1, 2]
data1 = [3, 4]

data_2D = [data0,data1,10]
data_2D_copy = data_2D.copy()

print("\n===Address Member ke-satu===\n")
print(f"Address asli = {hex(id(data_2D[0]))}")
print(f"Address copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# Pakai deep copy untuk merubah address member, biar ga satu dirubah semuanya
# berubah

from copy import deepcopy

data_2D = [data0,data1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"Address asli = {hex(id(data_2D))}")
print(f"Address deep = {hex(id(data_2D_deepcopy))}")


print("\n===Address Member ke-satu===\n")
print(f"Address asli = {hex(id(data_2D[0]))}")
print(f"Address copy = {hex(id(data_2D_deepcopy[0]))}")


data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")