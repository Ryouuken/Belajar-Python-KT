# data yang di input pasti bertipe string

data = input("masukan nama :")

print("data :", data,"type :", type(data))

#bagaimana kalo mau datanya jadi integer, bisa kita casting dulu
angka = int(input("masukan angka :"))


print("data:", angka, "type :", type(angka))

#kalo float?
angka = float(input("masukan angka :"))
print("data:", angka, "type :", type(angka))

#kalau boolean? dalam bineraja ya jadi 1 dan 0
# untuk boolean kita harus ubah dulu ke integer

biner = bool(int(input("masukan angka biner :")))

print("data :", biner, "type :", type(biner))
