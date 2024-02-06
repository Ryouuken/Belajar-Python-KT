import datetime as dt
import os
import string
import random

#template mahasiswa
mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "sks_lulus":0,
    "lahir":dt.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["nama"] = input("Nama Mahasiswa: ")
    mahasiswa["nim"] = input("NIM Mahasiswa: ")
    mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun lahir (yyyy):"))
    BULAN_LAHIR = int(input("Bulan lahir (1-12):"))
    TANGGAL_LAHIR = int(input("tanggal lahir (1-31):"))
    mahasiswa["lahir"] = dt.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY= ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'NAMA':<17} {'NIM':<12} {'SKS':<3} {'LAHIR':<10}")
    print("-"*57)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<12} {SKS:<3} {LAHIR:<10}")

    print("\n")
    is_done = input("sudah beres bro? (y/n)")
    if is_done == "y":
        break

print("akhir dari program, terimakasih.")
