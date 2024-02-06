#latihan konversi satuan temperature

## program konversi celcius ke satuan temperature lainnya
print("\n-------CELCIUS------\n")

celcius = float(input("Masukan suhu dalam Celcius :"))
print("Suhu adalah :", celcius, "Celcius")

#Reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah :", reamur, "Reamur")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah :", fahrenheit, "Fahrenheit")

#Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah :", kelvin, "Kelvin")

##program konversi reamur ke satuan lain
print("\n-------REAMUR------\n")

reamur = float(input("masukan suhu dalam reamur :"))
print("Suhu adalah :", reamur, "Reamur")

#celcius
celcius = (5/4) * reamur
print("Suhu dalam Celcius adalah :", celcius, "Celcius")

#Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam Fahrenheit adalah :", fahrenheit, "Fahrenheit")

#Kelvin
kelvin = ((5/4) * reamur) + 273
print("Suhu dalam Kelvin adalah :", kelvin, "Kelvin")

##program konversi Fahrenheit ke satuan lain
print("\n-------Fahrenheit------\n")

fahrenheit = float(input("masukan suhu dalam Fahrenheit :"))
print("Suhu adalah :", fahrenheit, "Fahrenheit")

#Celcius
celcius = 5/9 * (fahrenheit - 32)
print("Suhu dalam Celcius adalah :", celcius, "Celcius")

#Reamur
reamur = 4/9 * (fahrenheit - 32)
print("Suhu dalam Reamur adalah :", reamur, "Reamur")

#Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah :", kelvin, "Kelvin")

##program konversi Kelvin ke satuan lain
print("\n-------Kelvin------\n")

kelvin = float(input("masukan suhu dalam Kelvin :"))
print("Suhu adalah :", kelvin, "Kelvin")

#Celcius
celcius = kelvin - 273
print("Suhu dalam Celcius adalah :", celcius, "Celcius")

#Reamur
reamur = 4/5 * (kelvin - 273)
print("Suhu dalam Reamur adalah :", reamur, "Reamur")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah :", fahrenheit, "Fahrenheit")

