#Break, jadi kalo sudah ketemu break, selanjutnya bakalan di skip ke program berikutnya, ga loop lagi

#contoh 1

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    if angka == 3:
        print("Goks !")
        break
    print("Whassup guis !")

print("Sudah cukup !")

#contoh 2

data_int = int(input("Masukan mau angka berapa men : "))

angka = 0

while True:
    angka += 1
    print(f"Angka sekarang {angka}")
    if angka == data_int:
        break

print("Dah cukup !")