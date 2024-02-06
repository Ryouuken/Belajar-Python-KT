#operasi

#Index   0(-3)   1(-2)     2(-1)
data = ["Ucup", "Otong", "Dudung"]

#Mengambil data dari list
print("\n====mengambil data====\n")
## ambil data dari index ke - 0 atau si ucup
data_0 = data[0]
print(f"ini adalah data dari index ke 0 -> {data_0}")
## ambil data terakhir, kalo datanya panjang kita pake indexnya -1 aja untuk data terakhir
data_terakhir = data[-1]
print(f"ini adalah data paling akhir dari list -> {data_terakhir}")

# Mengambil info jumlah data dari list
print("\n====mengambil Info Jumlah data====\n")
panjang = len(data)
print(f"berikut adalah jumlah data dari list = {panjang}")

#manipulasi data list
print("\n====Manipulasi data====\n")

#Menambah item di posisi sesuai list
print(f"list sebelum dimanipulasi = {data}")

#menambahkan data pada list sesuai index
print("\n====Menambah data (insert)====\n")
data.insert(1,"Asep")
print (f"ini data setelah ditambah Asep pada index ke 1 = {data}")

#Menambah data dari paling belakang 
print("\n====Menambah data dari paling belakang (append)====\n")
data.append("Jajang")
print(f"data ditambahkan lagi dari paling belakang = {data}")

#Menambah list dengan list
print("\n====Menambah data list dengan list lainnya (extend)====\n")
data_baru = ["Maman", "Kipli", "Romlah"]
data.extend(data_baru)
print(f"menambahkan list dengan list lainnya jadinya = {data}")

#Merubah data dari suatu list, kita coba ubah data dari index ke 2 dari 'otong' menjadi 'michael'
print("\n====Mengubah data dari suatu list====\n")
data[2] = "Michael"
print(f"data pada index ke 2 berubah menjadi = {data}")

#Meremove data 
print("\n====Meremove data====\n")
data.remove("Jajang")
print(f"meremove salah satu data dari list, si 'jajang' = {data} ")

#Meremove data paling belakang
print("\n====Meremove data paling belakang====\n")
data.pop()
print(f"meremove data yang paling belakang = {data}")
