# Operator dalam bentuk methods
## Merubah Case (besaran huruf)

### Merubah semua ke huruf besar (Upper Case)
print("\n====UpperCase====\n")
data = "Kemarin aku tidur"
print("normal =", data)
print("upper =", data.upper())





### Merubah semua ke huruf kecil (Lower Case)
print("\n====LowerCase====\n")
alay = "Aku KecE AbbieeZzzZzzZZZ"
print("normal =", alay)
print("lower =", alay.lower())

##Pengecekan dengan is method
print("\n====Check LowerCase====\n")
#Contoh pengecekan lowercase
salam = "bro"
is_lower = salam.islower()
print(salam, "adalah lower =", is_lower)
#Contoh pengecekan Uppercase
print("\n====Check LowerCase====\n")
is_upper = salam.isupper()
print(salam, "adalah upper =", is_upper)

#isalpha() <-- untuk mengecek semua huruf
print("\n====Check Isalpha====\n")
alpha = "halobrobrosemuanya" # jadi semua huruf, gaboleh ada angka dan spasi atau tanda apapun
cek_alpha = alpha.isalpha()
print(alpha, ", adalah is alpha = ", cek_alpha) 

#isalnum() <-- untuk mengecek huruf dan angka
print("\n====Check Isnum====\n")
alnum = "izan10" # Jadi selama ada angka atau huruf, tanpa spasi atau tanda lainnya, dia true
cek_alnum = alnum.isalnum()
print(alnum, ", adalah is alnum = ", cek_alnum) 

#isdecimal() <-- angka saja
print("\n====Check Isdecimal====\n")
decimal = "08985658936" # Jadi semua hanya boleh angka, tanpa huruf,spasi atau apapun
cek_decimal = decimal.isdecimal()
print(decimal, ", adalah is decimal = ", cek_decimal) 

#isspace() <-- spasi, tab, newline(\n) SAJA
print("\n====Check Isspace====\n")
space = "   \n" # Jadi hanya boleh kosong, atau spasi, tab, \n yang tak terlihat
cek_space = space.isspace()
print(space, ", adalah is space = ", cek_space) 

#istitle() <-- semua kata dimulai dengan huruf besar
print("\n====Check Istitle====\n")
judul = "It Is Okay To Not To Be Okay"
cek_judul = judul.istitle()
print(judul, ", adalah is title = ", cek_judul)

## Mengecek komponen Startswith dan Endswith
print("\n====Check Startswith&Endswith====\n")
starts = "Hello Everybody".startswith("Hello")
print("Start =", starts)
ends = "Moshi Moshii".endswith("Moshii")
print("Ends = ", ends)

## Komponen join dan split memakai list ([])
print("\n====Join====\n")
pisah = ["aku", "sayang", "kamu"]
gabungan = ",".join(pisah) 
print(gabungan) # jadi dipisah perkata memakai tanda ,

gabungan = " ".join(pisah)
print(gabungan) # jadi dipisah perkata memakai tanda " " (Spasi)

gabungan = " ehm ".join(pisah)
print(gabungan) # jadi dipisah perkata memakai kata "ehm"

print("\n====Split====\n")
gabungan = "akuehmsayangehmkamu"
print(gabungan.split("ehm")) # dan dia kembali pada bentuk list lagi

##Alokasi karakter ljust(), rjust(), center()
print("\n====alokasi karakter====\n")
left = "left".ljust(10) # artinya bakal ada 10 karakter, nah di 4 karakter pertama itu ada string "left"
print("'",left,"'") # 6 karakter sisanya akan kosong atau sesuai syntax

right = "right".ljust(10) # artinya bakal ada 10 karakter, nah di 4 karakter pertama itu ada string "right"
print("'",right,"'") # 6 karakter sisanya akan kosong atau sesuai syntax

###Terus kalau mau kanan kirinya ada tandanya bisa ga? bisa, begini caranya
center = "center".center(20, "+")
print("'",center,"'")

### Terus kalo mau ngehapus tandanya gimana?, begini
center = center.strip("+") # jadi kalo yang tadinya ada tandanya , harus disertakan lagi tandanya
print("'",center,"'")
### sudah kan. terus kalo yang kanan atau kiri si sisi kosongnya bisa diilangin juga? bisa dong
left = left.strip() # untuk ini ga perlu mention tanda lagi, karena emang diawal dia ga dikasih tanda
print("'",left,"'")