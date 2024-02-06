a = 10
b = 3

#operasi pertambahan
hasil = a + b
print(a, "+", b, "=", hasil)

#operasi pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

#operasi perkalian
hasil = a * b
print(a, "*", b, "=", hasil)

#operasi pembagian
hasil = a / b
print(a, "/", b, "=", hasil)

#operasi eksponen (pangkat)
hasil = a ** b
print(a, "**", b, "=", hasil)

#operasi modulus (sisa pembagian)
hasil = a%b
print(a, "%", b, "=", hasil)

#operasi floor division (kebalikan modulus)
hasil = a//b
print(a, "//", b, "=", hasil)

## prioritas operasi, operational precedence
### prioritas operasi atau yang dihitung duluan yaitu :
### tanda ()
### eksponen
### perkalian, pembagian, eksponen, floor division. (satu level mereka semua)
### pertambahan dan pengurangan

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x

print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x, "=", hasil)

