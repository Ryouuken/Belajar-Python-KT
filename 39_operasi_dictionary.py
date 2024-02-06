#operator dictionary

data_dict = {
    "cup": "ucup surucup",
    "tong": "otong surotong",
    "dung": "dudung surudung"

}

lendict = len(data_dict)
print(f"panjang data dict adalah : {lendict}")

## kita pastikan apakah suatu data ada pada dictionary

key = "ucup"
checkkey = "cup" in data_dict

print(f"apakah {key} ada dalam data dict : {checkkey}")

# Mengakses value dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan")) #cek key dengan message tidak ditemukan
# dengan pakai .get(), bila suatu data tidak ada dalam dictionary maka akan di return
# dengan None, bisa tidak pakai .get() maka yang terjadi adalah error

#mengupdate data

data_dict.update({"cup":"ucup si siu"}) # jadi kalau datanya udah ada, maka akan di update
print(data_dict)
data_dict.update({"hafiz":"hafiz sipaling keren"})# bila data belum ada maka akan langsung di add 
print(data_dict) # ketika menggunakan.update

# Mendelete data dalam dictionary
del data_dict["hafiz"]
print(data_dict)