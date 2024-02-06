#operasi komparasi adalah untuk membandingkan nilai

# setiap hasil dari operasi komparasi adalah boolean

#>,<,>=,<=,==,!=,is,is not

a = 4
b = 2

#Lebih besar dari (>)
print("\n=====Lebih besar dari (>)=====\n")

hasil = a > 3
print(a,">",3,"=", hasil)

hasil = a > 4
print(a,">",4,"=", hasil)

hasil = b > 3
print(b,">",3,"=", hasil)

#kurang dari (<)
print("\n=====kurang dari (<)=====\n")

hasil = a < 3
print(a,"<",3,"=", hasil)

hasil = a < 4
print(a,"<",4,"=", hasil)

hasil = b < 3
print(b,"<",3,"=", hasil)

#lebih dari sama dengan (>=)
print("\n=====Lebih dari sama dengan (>=)=====\n")

hasil = a >= 3
print(a,">=",3,"=", hasil)

hasil = a >= 4
print(a,">=",4,"=", hasil)

hasil = b >= 3
print(b,">=",3,"=", hasil)

#kurang dari sama dengan(<=)
print("\n=====Kurang dari sama dengan (<=)=====\n")

hasil = a <= 3
print(a,"<=",3,"=", hasil)

hasil = a <= 4
print(a,"<=",4,"=", hasil)

hasil = b <= 3
print(b,"<=",3,"=", hasil)

#sama dengan (==)
print("\n=====Sama dengan (==)=====\n")

hasil = a == 3
print(a,"==",3,"=", hasil)

hasil = a == 4
print(a,"==",4,"=", hasil)

hasil = b == 3
print(b,"==",3,"=", hasil)

#Tidak sama dengan (!=)
print("\n=====Tidak sama dengan (!=)=====\n")

hasil = a != 3
print(a,"!=",3,"=", hasil)

hasil = a != 4
print(a,"!=",4,"=", hasil)

hasil = b != 3
print(b,"!=",3,"=", hasil)

#is adalah object identity
#is itu untuk membandingkan objek, contohnya si 4 itu literal, jadi ga bisa dibandingkan, yang termasuk
#objek itu si a, b , pokoknya variabel yang mempunyai nilai , itu objek a is b, itu bisa tapi kalau
# a is 4 itu ga bisa
print("\n=====Object Identity (is)=====\n")

x = 5 # ini adalah assignment membuat objek
y = 5
print("nilai x =", x, "id =", hex(id(x))) 
print("nilai y =", y, "id =", hex(id(y)))
# dapat dilihat bahwa si x dan y disimpan di id yang sama karena nilai mereka sama sama 5
# maka x is y hasilnya adalah true, bahwa mereka itu sama

hasil = x is y
print("x is y =",hasil)

x = 5 # ini adalah assignment membuat objek
y = 6
print("nilai x =", x, "id =", hex(id(x))) 
print("nilai y =", y, "id =", hex(id(y)))
#dapat dilihat untuk si y dia sekarang berbeda id nya, karena nilainya pun berbeda, maka x is y adalah false

hasil = x is y
print("x is y =",hasil)

#is not adalah object identity

print("\n=====Object Identity (is not)=====\n")

x = 5 # ini adalah assignment membuat objek
y = 5
print("nilai x =", x, "id =", hex(id(x))) 
print("nilai y =", y, "id =", hex(id(y)))
# dapat dilihat bahwa si x dan y disimpan di id yang sama karena nilai mereka sama sama 5
# maka x is y hasilnya adalah true, bahwa mereka itu sama

hasil = x is not y
print("x is y =",hasil)

x = 5 # ini adalah assignment membuat objek
y = 6
print("nilai x =", x, "id =", hex(id(x))) 
print("nilai y =", y, "id =", hex(id(y)))
#dapat dilihat untuk si y dia sekarang berbeda id nya, karena nilainya pun berbeda, maka x is y adalah false

hasil = x is not y
print("x is y =",hasil)

# lihat, hasilnya yang berbeda menjadi true, sedangkan yang sama jadi false, ini terbalik dengan is