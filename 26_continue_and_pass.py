#continue, pass

#pass -> berfungsi sebagai dummy, dia tidak akan dieksekusi
print("====Pass====")
angka = 0

while angka <5:
    angka += 1
    if angka == 3:
        pass
    print(angka)

#Continue
print("\n====Continue====")

angka = 0
print(f"angka sekarang -> {angka}")

while angka <5 :
    angka += 1
    print(f"angka sekarang -> {angka}") # -> Aksi 1
    if angka == 3:
        print("NT bang")
        continue # jadi kalo ada si continue, aksi 2 dan selanjutnya pada si loop tsb akan di lewatkan, balik lagi ke atas

    print("Whassup my friend") # -> Aksi 2

print("Sudah cukup")