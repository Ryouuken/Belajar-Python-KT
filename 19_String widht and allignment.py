## String and multiline

#Data
print("\n====Data====\n")
data_nama = "ucup surucup"
data_umur = 17
data_tinggi = 151.1
data_sepatu = 42

# String standard
print("\n====String Standard====\n")
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_sepatu}"
print(data_string)

#String multiline , (pakai enter, \n)
print("\n====String Multiline dengan enter (\n)====\n")
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_sepatu}"
print(data_string)

#String multiline (kutip triplet)
print("\n====String Multiline dengan kutip triplet====\n")
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_sepatu}
"""

print(data_string)

#mengatur lebar
print("\n====Mengatur lebar====\n")
data_nama = "ucup"
data_string = f"""
nama   = {data_nama}
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_sepatu:>5}
"""
#membuat rata kanan tapi kalo jumlah string lebih besar dari yang ditentukan dia hanyaakan mengisi (geser)
#tapi liat yang jumlah stringnya kurang dari 5, dia akan jadi rata kanan semua 
print(data_string)