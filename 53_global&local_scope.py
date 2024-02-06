import os

print(os.system("cls"))

## Global dan local scope
## Variabel Global dia bisa hidup dimana saja
## Variabel Local dia hanya hidup di dalam fungsi

#akses variabel global dalam fungsi
print("===Global Scope===\n")
nama_global = "otong" # <- ini variabel global

def fungsi1():
    print(f"fungsi ini menampilkan {nama_global}")

fungsi1()

#akses variabel global dalam loop

for i in range(0,5):
    print(f"loop {i} - {nama_global}")

#percabangan 
if True:
    print(f"ini menampilkan {nama_global}")

## Variabel Local Scope
print("\n===Local Scope===\n")

def fungsi2():
    nama_local = "Ucup" # <~ ini variabel local
    print(nama_local)

fungsi2()

## Contoh 1: penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()

## Contoh 2: merubah variabel global
angka = 0
name = "Ucup"

def ubah(angka_baru, nama_baru):
    global angka # fungsi ini mendapat akses merubah variabel global
    global name
    angka = angka_baru
    name = nama_baru

print(f"sebelum {angka,name}")
ubah(10,"Dudung")
print(f"Sesudah {angka,name}")

## Contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0


print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)

## kesimpulannya local variabel bisa diakses langsung bila dia dibuat
## di dalam if atau for dsb, namun bila local variabel hidupnya
## didalam fungsi, dia tidak bisa diakses dari luar