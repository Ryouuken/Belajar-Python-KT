# Teknik menduplikat list

a = ["Ucup", "Otong", "Dudung"]

print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

#kita akan merubah member dari a
# ini akan merubah kedua list
print("\n===Merubah list===\n")

a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list
print("\n===Address list a dan b===\n")

print(f"address dari a = {hex(id(a))}")
print(f"address dari b = {hex(id(b))}")
## bisa dilihat bahwa kedua list ini mempunyai address yang sama, jadi ketika kita mengubah salah satunya
## maka yang satunya juga akan ikut berubah

#Menduplikat list dengan copy
print("\n===Menduplikat dengan copy()===\n")
c = a.copy() # full duplicate / data baru

print(f"address dari a = {hex(id(a))}")
print(f"address dari b = {hex(id(b))}")
print(f"address dari c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("\n===Pembuktian ke 1\n")
print("kita ubah data ke 0")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
## bisa dilihat di terminal bahwa pada index ke 0 untuk list c sudah berubah jadi Dadang namun list a dan b
## masih tetap Dudung, jadi mereka tidak berpengaruh, contoh lainnya adalah:

print("\n===Pembuktian ke 2\n")
print("kita ubah data ke 1")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
## bisa dilihat bahwa index ke 1 untuk list a dan b dia berubah menjadi Otong lagi sedangkan list c masih
## tetap Michael, ini terjadi karena list c tidak menggunakan address yang sama dengan a dan b.