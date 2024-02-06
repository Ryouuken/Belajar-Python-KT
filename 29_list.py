# cara membuat list

#list numbers
print("===Numbers===")
list_angka = [1,2,3,4]
print(list_angka)

#list string
print("\n===String===")
list_string = ["ucup", "otong", "odah"]
print(list_string)

#list boolean
print("\n===Boolean===")
list_boolean = [True, False, True, True]
print(list_boolean)

#list Campuran
print("\n===Campuran===")
list_campuran = [2, "martabak", 1, "penjual", "ucup", True]
print(list_campuran)

#Alternatif membuat list
#range
print("\n===Pakai Range===")
data_range = range(0 , 10, 2) # Start, Stop, Step

data_list = list(data_range)
print(data_list)

#pakai for loop, terus coba kita buat angkanya berpangkat
print("\n===Pakai for loop===")
## coba kita pangkatin tiap angkanya 3
data_for_loop = [i ** 3 for i in range (0,10)]
print(data_for_loop)


## pakai for pake if
print("\n===Pakai for pake if===")
#coba kita ilangin angka 5 dalam list nya
data_for_if = [i for i in range(0,10) if i != 5]
print(data_for_if)

#kita cari angka angka genap
print("\n===Pakai for pake if untuk cari genap===")
data_for_if = [i for i in range(0,10) if i%2 == 0]
print(data_for_if)

#kita cari angka ganjil
print("\n===Pakai for pake if untuk cari ganjil===")
data_for_if = [i for i in range(0,10) if i%2 != 0]
print(data_for_if)