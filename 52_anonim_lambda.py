import os

print(os.system("cls"))

#lambda function

print("===Tanpa Lamda===\n")
def f_kuadrat(angka):
    return angka**2

print(f"hasil dari kuadrat = {f_kuadrat(3)}")

print("\n===Dengan Lamda===\n")
## sekarang kita pakai lambda

kuadrat = lambda angka:angka**2

print(f"hasil dari kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow: num**pow

print(f"hasil dari pangkat = {pangkat(6,2)}")

## kegunaan apa bang?
print("\n===Contoh penggunaan===\n")

print("\n===Sorting===\n")
#sorting untuk list biasa

data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

#sorting dengan panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang = {data_list}")

# sorting pakai lambda
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")

print("\n===Filter===\n")
#filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

### tanpa lambda
def kurdar5(angka):
    return angka<5

data_angka_baru = list(filter(kurdar5,data_angka))
print(data_angka_baru)

### dengan lambda
data_angka_baru = list(filter(lambda x:x<8, data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:x%2==0,data_angka))
print(data_genap)

#kasus ganjil
data_ganjil = list(filter(lambda x:x%2 !=0,data_angka))
print(data_ganjil)

#kelipatan 3
kelipatan3 = list(filter(lambda x:x % 3 == 0, data_angka))
print(kelipatan3)

print("\n===Anonymous Function===\n")
# anonymous function
#currying <- Haskell Curry

def pangkat (angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(data_hasil)

#dengan currying
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 =  {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat 2 =  {pangkat2(3)}")
## bisa juga langsung gini dengan pangkat bebas
print(f"pangkat bebas = {pangkat(4)(5)}")
#### jadi si 4 itu jadi pangkatnya, 5 nya jadi si angka yang mau dipangkatkannya

