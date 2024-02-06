data_angka = [1, 2, 0, 5, 2, 6, 7, 4, 10, 23, 5, 6, 7]

print(f"data angka = {data_angka}")

# count data
print("\n===COUNT===\n")
data_angka_4 = data_angka.count(4)
data_angka_5 = data_angka.count(5)

print(f"data angka 4 = {data_angka_4}")
print(f"data angka 5 = {data_angka_5}")

# ambil posisi data
print("\n===Posisi Data===\n")

data = ["Ucup", "Otong", "Dudung", "Ujang"]

print(f"data = {data}")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")

print(f"data index Dudung = {index_dudung}")
print(f"data index Ujang = {index_ujang}")

#Mengurutkan list (diurutkan berdasarkan terkecil ke terbesar)
print("===Sorting List===")

print(f"data angka sebelum di sort = \n{data_angka}")

data_angka.sort()
print(f"data angka setelah di sort\n{data_angka}")

## list string (diurutkan berdasarkan abjad)
print(f"data sebelum disort \n{data}")
data.sort()
print(f"data setelah disort \n{data}")

## Reverse data (kalau mau print data sort nya terbalik)
## jangan lupa sebelum di reverse, biar rapih, di sort dulu yaa
data_angka.reverse()
data.reverse()
print(f"Data yang direverse = \n{data_angka}, \n{data}")