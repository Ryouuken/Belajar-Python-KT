# exception akan terjadi saat program mengalami error saat runtime

## contoh sederhana untuk menangkap error
# data_input = int(input("Masukan angka: "))

# hasil = 0

# try:
#     hasil = 10/data_input
# except:
#     print("Hasil tidak boleh 0")

# print(f"hasil = {hasil}")

## contoh di aplikasi

# while True:
#     angka = int(input("Masukan angka pembagi: "))
#     try:
#         hasil = 10/angka
#         print(f"hasil = {hasil}")
#         is_done = input("lanjutkan (y/n)? ")
#         if is_done == "n":
#             break
#     except:
#         print("Angka pembagi 0, silahkan input lagi")

# print("akhir dari program")

## contoh aplikasi untuk membuat file data.txt
try:
    with open("data_4.txt","r") as file:
        print(file.read())
except:
    print("file tidak ditemukan membuat file baru")
    with open("data_4.txt","w",encoding='utf-8') as file:
        file.write("file baru")

print("akhir dari program")