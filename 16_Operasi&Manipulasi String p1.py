#1. Menyambung string (Concatenate)
print("\n====Concatenate====\n")
nama_depan = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_depan +" "+ nama_tengah + "'" + nama_akhir
print(nama_lengkap)

#2. Menghitung panjang string (len())
print("\n====Len====\n")
panjang = len(nama_lengkap)
print("Panjang string dari", nama_lengkap + " =", str(panjang))

#3.Operator untuk string
## Mengecek apakah char atau string ada di suatu string
print("\n====Check String====\n")
d = "Ucup"
status = d in nama_lengkap
print("String ", d, "ada di", nama_lengkap, " =", str(status))

d = "Ucup"
status = d not in nama_lengkap
print("String ", d, "ada di", nama_lengkap, " =", str(status))

##Mengulang string
print("\n====Repeat String====\n")
print("wk"*10)
print(15*"wk")

##Indexing
print("\n====Indexing====\n")
print("Index ke-0 :", nama_lengkap[0])
print("Index ke-6 :", nama_lengkap[6])
print("Index ke-(-1) :", nama_lengkap[-1])
print("Index ke-(-2) :", nama_lengkap[-2])
### kalau mau indexing dari sekian sampai sekian, itu harus di + 1 in, jadi kalo mau index 0 sampai 3
### harus bikinnya [0:4] sampai 4 di syntaxnya, karena dia yang index terakhirnya ga dimasukin (sebagai stopper)
print("Index ke 0 sampai 3 :", nama_lengkap[0:4])
print("Index ke 3 sampai 7 :", nama_lengkap[3:8])
### terus kalo mau indexnya di jeda jeda bisa ga? bisa dong, misalkan mau dijeda per 2 gitu ya
print("Index ke-[0,2,4,6,8,10] :", nama_lengkap[0:11:2])

## item terbesar
print("\n====Item terbesar====\n")
print("paling besar :", max(nama_lengkap))
## item terkecil
print("\n====Item terkecil====\n")
print("paling besar :", min(nama_lengkap))

print("\n====pembuktian terbesar dan terkecil dengan ascii code====\n")
ascii_code = ord(" ")
print("ASCII code untuk string spasi adalah :", str(ascii_code))
ascii_code = ord("u")
print("ASCII code untuk string spasi adalah :", str(ascii_code))
### bisa dilihat si spasi ascii codenya adalah 32, lebih kecil dibandingkan si U yang bernilai 117
### kalau ingin mencari karakter dari besaran ASCII nya gimana? gini caranya
data = 117
print("Char untuk ASCII 117 adalah :", chr(data))
### bener ya, ASCII yang bernilai 117 itu adalah charackter u

## 4. Operator dalam bentuk method, contohnya biasanya ada tanda . nya, contoh (string.count())
data = "otong surotong pararotong"
### coba kita cari berapa banyak huruf o pada string di data menggunakan method count, btw method ada banyak ya
jumlah = data.count("o")
print("Jumlah string 'o' pada", data, "adalah =", str(jumlah))