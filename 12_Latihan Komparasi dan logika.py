### membuat gabungan area rentang dari angka

## ++++++3--------------------10++++++++
inputuser = float(input("Masukan angka kurang dari 3 atau lebih dari 10 :"))

## memeriksa angka kurang dari 3

kurdar = (inputuser < 3)

print("Kurang dari 3 = ", kurdar)

## memeriksa angka lebih dari 10

lebdar = (inputuser > 10)

print("Lebih dari 10 = ", lebdar)

## ++++++3--------------------10++++++++

hasil = kurdar or lebdar
print("angka yang anda masukan: ", hasil)

print("\n=======================\n")
### membuat irisan area rentang dari angka

##------------3++++++++++++10-----------
inputuser = float(input("Masukan angka lebih dari 3 dan kurang dari 10 :"))

## memeriksa angka lebih dari 3
lebdar = inputuser > 3
print("Lebih dari 3 = ", lebdar)

## memeriksa kurang dari 10
kurdar = inputuser < 10
print("Kurang dari 10 = ", kurdar)

## --------3+++++++++++++10-----------
hasil = lebdar and kurdar
print("angka yang anda masukan:" , hasil)

print("\n=======================\n")
### PR
## PR no 1
## -----0++++++5-------8++++++++11-----------
pr = float(input("Masukan angka diantara 0 sampai 5 atau 8 sampai 10 :"))
lebdar0kur5 = pr > 0 and  pr < 5
print("Lebih dari 0 kurang dari 5", lebdar0kur5)

lebdar8kur11 = pr > 8 and pr < 11
print("Lebih dari 8 kurang dari 11", lebdar8kur11)

hasilpr1 = lebdar0kur5 or lebdar8kur11
print("angka yang anda masukan : ", hasilpr1)
print("\n=======================\n")
##PR no 2
## ++++++0-------5++++++++8---------11+++++++++
pr2 = float(input("Masukan angka kurang dari 0 ,  5 sampai 8 dan lebih dari 10 :"))
kurdar0 = pr2 < 0
print("kurang dari 0 =", kurdar0)
lebdar5kur8 = pr2 > 5 and pr2 < 8
print("lebih dari 5 kurang dari 8 =", lebdar5kur8)
lebdar11 = pr2 > 11
print("Lebih dari 11 =", lebdar11)

hasilpr2 = kurdar0 or lebdar5kur8 or lebdar11
print("angka yang anda masukan :", hasilpr2)

print("\n=======================\n")