# multi keys
import datetime as dt

mahasiswa1 = {
    "nama":"Ucup Surucup",
    "nim":"181010503121",
    "sks_lulus":130,
    "beasiswa":False,
    "lahir":dt.datetime(2001,1,29)
}


mahasiswa2 = {
    "nama":"Otong Surotong",
    "nim":"181010503122",
    "sks_lulus":140,
    "beasiswa":True,
    "lahir":dt.datetime(2002,10,14)
}
mahasiswa3 = {
    "nama":"Dudung Surudung",
    "nim":"181010503123",
    "sks_lulus":100,
    "beasiswa":False,
    "lahir":dt.datetime(2000,5,20)
}

# Nested Dictionary
data_mahasiswa = {
    "MAH001":mahasiswa1,
    "MAH002":mahasiswa2,
    "MAH003":mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<12} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<10}")
print("-"*57)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {NIM:<12} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")