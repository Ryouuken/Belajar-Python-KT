# Looping pada list

## for loop
print("====For Loop====")
kumpulan_angka = [1,6,7,3,2,1,7]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

kumpulan_nama = ["ucup", "otong", "dadang", "maman", "usep"]

for nama in kumpulan_nama:
    print(f"nama = {nama}")

## Forloop dan range
print("\n====For Loop & Range====")

kumpulan_angka = [2,90,34,14,52]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

## While loop
print("\n====While Loop====")

kumpulan_angka = [2,90,34,14,52]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

#list comprehension
print("\n====List Comprehension====")
data = ["ucup",2,7,9,"dudung"]

[print(f"data={i}") for i in data]

angka = [2,90,34,14,52]

## bila mau membuat angka kuadrat pake list comprehension
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

#Enumerate
print("\n====Enumerate====")
data_list = ["ucup",2,7,9,"dudung"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
