## bitwise 
## jadi tentang angka binary gitu kayak 00000010
## 00000010 itu sama dengan integer 2, kenapa karena itungnya itu pangkat dari 2
## jadi karena 1 nya di 2 terakhir berarti jadi 2 pangkat 1 = 2
## kalau 0000001 itu int 1, karena 2pangkat 0 = 1, jadi yang 00000001 itu kaya kberdasarkan
## index gitu loh, angka paling belakang berarti index ke - 0, artinya kalo
## ada angka 1 di binarynya , artinya dia pangkat 0


##oke kita coba ya
a = 9
b = 5

## bitwise Or |
print("\n==============OR=============")
c = a|b
print("Nilai", a, ", binary :", format(a,"08b"))
## ya, jadi binary si integer 9 itu 00001001, karena berdasarkan indexnya jadi, inget angka 1 di akhir artinya
## pangkat 0 karena dia di index ke-0, jadi 2pangkat 0 ditambah 2 pangkat 3, karena angka 1 lagi di index ke-3
## hasilnya jadi 2pangkat 3 adalah 8 ditambah 1 jadinya 9
print("Nilai", b, ", binary :", format(b,"08b"))

print("----------------------OR (|)------------------")
print("Nilai", c, ", binary :", format(c,"08b"))
## kenapa 13? karena si binary a dan b dia di operasi logika kan pakai or, jadinya bisa diliat di index 0
## antara si nilai 9 dan 5, 1 or 1 hasilnya 1, 0 or 0 hasilnya 0, 0 or 1 hasilnya 1, terus ampe index terakhir
# hasilnya 00001101, berarti, 2pangkat 0 ditambah 2pangkat2 ditambah 2pangkat3, berarti 1+4+8 = 13

##bitwise AND &
print("\n==============AND=============")
c = a&b
print("Nilai", a, ", binary :", format(a,"08b"))
print("Nilai", b, ", binary :", format(b,"08b"))
print("----------------------AND (&)------------------")
print("Nilai", c, ", binary :", format(c,"08b"))
##Nilainya 1 karena logika and adalah, bila false ketemu true dia akan false, jadi kalo mau true, harus 
## True ketemu True, selain itu FALSEEE, makanya hasilnya 00000001, jadi 2 pangkat 0 = 1

##Bitwise XOR ^
print("\n==============XOR=============")
c = a^b
print("Nilai", a, ", binary :", format(a,"08b"))
print("Nilai", b, ", binary :", format(b,"08b"))
print("----------------------XOR (^)------------------")
print("Nilai", c, ", binary :", format(c,"08b"))
## yang XOR juga sama , kenapa 12 nilainya karena logika XOR adalah dia kalo mau true harus ketemu yang beda
## kayak 1 ketemu 0 = true, kalo 1 ketemu 1 atau 0 ketemu 0 dia jadinya FALSE

##Bitwise NOT ~
print("\n==============NOT=============")
c = ~a
print("Nilai :", a, ", binary :", format(a, "08b"))
print("----------------------NOT (~)------------------")
print("Nilai :", c, ", binary :", format(c, "08b"))

print("----------------------XOR (^)------------------")
d = 0b00001001
e = 0b11111111
print("Nilai", d)
print("Nilai", e^d, ", binary :", format(e^d,"08b"))
## kenapa nilainya -10, karena 0 itu dia ga punya mines kan , jadi dia mulainya dari -1, kan not itu atinya
## yang bukan, atau kebalikannya, sedangkanangka biner kan 0 ama 1, nah si 0 ga punya mines kan jadi mulainya dari -1
## jadi kalo kita punya int9 di not kan makahasilnya jadi -10, jadi angka int + (-1)
## kalaupun mau angka binernya beneran dibalik semua bisa, tapi pakai XOR lagi, jadinya :

## selanjutnya ada Shifting, maksudnya itu digeser, jadi nanti angka nya di geser pake tanda >> untuk kekanan
## dan << untuk geser ke kiri, liat aja deh hasilnya

#Shifting Right (Geser ke kanan)
print("\n==============>>=============")
c = a >> 2
print("Nilai :", a, ", binary :", format(a, "08b"))
print("------------->> Geser kanan------------------")
print("Nilai :", c, ", binary :", format(c, "08b"))
## Nah kegeser dah tuh angka binary nya kekanan 2 kali, kalo kekiri gimana? yaudah tinggal ubah tanda aja

#Shifting Right (Geser ke kiri)
print("\n==============<<=============")
c = a << 2
print("Nilai :", a, ", binary :", format(a, "08b"))
print("-------------<< Geser kiri------------------")
print("Nilai :", c, ", binary :", format(c, "08b"))