# 1. mode write,
# dia akan membuat file baru bila tidak ada file dengan nama yang kita tulis
# lalu akan akan menimpa atau overwrite isinya

with open("Kelas_terbuka_py/data.txt","w",encoding="utf-8") as file:
    file.write("Ucup surucup")

with open("Kelas_terbuka_py/data.txt","w",encoding="utf-8") as file:
    file.write("John si Johnny")

# 2. kalau mau nambah atau append pakai "a"
with open("Kelas_terbuka_py/data_2.txt","w",encoding="utf-8") as file:
    file.write("Ucup surucup\n")

with open("Kelas_terbuka_py/data_2.txt","a",encoding="utf-8") as file:
    file.write("John si Jhonny")

# 3. mode r+
with open("Kelas_terbuka_py/data_3.txt","w",encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("Kelas_terbuka_py/data_3.txt","r+",encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")

with open("Kelas_terbuka_py/data_3.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("Kelas_terbuka_py/data_3.txt","r+",encoding="utf-8") as file:
    file.write("otong\n") 
#jadi dia akan menimpa baris paling awal sesuai dengan panjang data
#misalkan baris-1 akan berubah jadi otong-1, karena data "baris"
#memiliki 5 karakter dan otong juga memiliki5 karakter, jadi tergantinya
#dari data "baris-1" hanya terganti 5 karakter
