# Kalkulator Sederhana
print("====Kalkulator Sederhana====\n")

angka_1 = float(input("Masukan angka pertama = "))
operator = input("Masukan operator (+,-,*,/) :")
angka_2 = float(input("Masukan angka kedua = "))

#percabangannya
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "*" or operator =="x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else :
    print("Yang bener ajalah")
print("Akhir dari program")