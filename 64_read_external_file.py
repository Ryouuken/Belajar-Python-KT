# Tutorial membaca file external


print("===Membaca file txt===\n")

file = open("Kelas_terbuka_py/data.txt",mode="r")

## Baca seluruh file
print(file.read())

## baca perbaris
print(file.readline(),end="") # baca baris pertama
print(file.readline(),end="") # baca baris kedua

## baca semua baris sebagai list
print(file.readlines())

### jangan lupa di close setelah di buka
print(f"apakah sudah di close? = {file.closed}")
file.close()
print(f"apakah sudah di close? = {file.closed}")

### salah satu teknik membuka file di python

print("\n===Membaca file txt dengan with===\n")

with open("Kelas_terbuka_py/data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah sudah di close? = {file.closed}") # disini dia masih terbuka

print(f"apakah sudah di close? = {file.closed}") # tetapi disini dia langsung tertutup
# jadi sudah tidak perlu nge close manual