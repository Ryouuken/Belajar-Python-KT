import os

print(os.system("cls"))

'''args'''

#memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} dengan tinggi {tinggi}, dan berat {berat}")

fungsi("ucup",170,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} dengan tinggi {tinggi}, dan berat {berat}")

fungsi(["otong",100,120])

#kenalan dengan args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} dengan tinggi {tinggi}, dan berat {berat}")

fungsi("dudung",200,30)

#studi kasus

#jadi penggunaan args tidak harus pakai (*args), bisa apa saja yang penting
# depannya dikasih tanda *, contohnya ini (*data)
def tambah(*data):
    #data tipenya adalah tuple, jadi bisa diiterasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil = {hasil}")

hasil = tambah(200,80,20)
print(f"Hasil = {hasil}")

#jadi kalau pake args kita ga perlu nentuin di bagian argument nya ada berapa yang
# bisa kita tambah, jadi bebas mau berapapun 