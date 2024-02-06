# Operasi yang dapat dilakukan dengan penyingkatan
## Operasi ditambah dengan assignment, contohnya
a = 10 # ini assignment
print("nilai a =", a)

a = 10
a = a+1 # ini operasi assignment tapi belum disingkat, nah ini bisa disingkat jadi
print("nilai a =", a)

print("\n====Tambah====\n")
a = 10
a += 1 # ini artinya sama aja kayak a = a+1, nih buktinya kal odi print bakal jadi,
print("nilai a += 1 adalah :", a)
# nilainya sama sama 11, sama aja, cuma ini lebiih singkat

## pengurangan
print("\n====Kurang====\n")
a = 10
a -= 2
print("nilai a -= 2 adalah :", a)

## perkalian
print("\n====Kali====\n")
a = 10
a *= 2
print("nilai a *= 2 adalah :", a)

## Pembagian
print("\n====Bagi====\n")
a = 10
a /= 2
print("nilai a /= 2 adalah :", a)

## Modulus (sisa)
print("\n====Modulus====\n")
b = 20
b %= 9
print("nilai b %= 9 adalah :", b)

## Floor Division
print("\n====Floor Division====\n")
b = 20
b //= 3
print("nilai b //= 3 adalah :", b)

## Pangkat
print("\n====Pangkat====\n")
b = 20
b **= 3
print("nilai b **= 3 adalah :", b)

###Operasi bitwise
##OR
print("\n====OR====\n")
c = True
print("nilai c = ", c)
c |= False
print("Nilai c |= False, nilai c menjadi: ", c)
## kenapa true? karena true or false hasilnya pasti true, kalo mau false harus false or false
c = False
print("nilai c = ", c)
c |= False
print("Nilai c |= False, nilai c menjadi: ", c)

##AND
print("\n====AND====\n")
c = True
print("nilai c = ", c)
c &= False
print("Nilai c &= False, nilai c menjadi: ", c)
## kenapa false? karena true and false hasilnya pasti false, kalo mau true harus True and True
c = True
print("nilai c = ", c)
c &= True
print("Nilai c &= True, nilai c menjadi: ", c)

##XOR
print("\n====XOR====\n")
c = True
print("nilai c = ", c)
c ^= False
print("Nilai c ^= False, nilai c menjadi: ", c)
## kenapa True? karena true XOR false hasilnya pasti true, begitu pula dengan false XOR True
## pokoknya kalo XOR itu yang beda, hasilnya pasti True, kalo yang sama, kayak : True XOR True, hasilnya pasti False 
c = True
print("nilai c = ", c)
c ^= True
print("Nilai c ^= True, nilai c menjadi: ", c)

##Shifting (Geser")
## Shifting Right
print("\n====Shifting Right====\n")
d = 0b0100
print("nilai d =", format(d, "04b"))
d >>= 2 
print("nilai d >>= 2, nilai d menjadi :", format(d, "04b"))
## Shifting Left
print("\n====Shifting Left====\n")
d <<= 1 
print("nilai d <<= 1, nilai d menjadi :", format(d, "04b"))
