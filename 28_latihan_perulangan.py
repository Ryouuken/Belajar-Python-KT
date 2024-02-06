#Latihan perulangan membuat segitiga

#menggunakan for
print("====For====")

sisi = 10
count = 1

for i in range(sisi):
    print("*"*count)
    count+= 1

# Menggunakan while
print("\n====While====")

count = 1
while True:
    print("*"*count)
    count +=1
    if count > sisi:
        break

# Membuat yang ganjil saja
print("\n====Ganjil====")

count = 1
while True:
    #print jika ganjil
    if count % 2:
        print("*"*count)
        count +=1
    else:
        count += 1
        continue
    

    #akan break jika count melebihi sisi
    if count > sisi:
        break

# Membuat segitiga sama kaki
print("\n====Segitiga sama kaki====")

count = 1
spasi = int(sisi/2)


while True:
    #untuk segitiga atasnya
    if count % 2:
        print(" "*spasi,"+"*count)
        spasi -= 1
        count +=1
    else:
        count += 1
        continue
    #untuk segitiga bawahnya
    if count > sisi:
        break

#Membuat ketupat
print("\n====Ketupat====")
sisi = 10
count = 1
spasi = int(sisi/2)


while True:
    #untuk segitiga atasnya
    if count % 2:
        print(" "*spasi,"+"*count)
        spasi -= 1
        count +=1
    else:
        count += 1
        continue

    if count > sisi:
        break

#untuk segitiga bawahnya
sisi = 10
count2 = 11
spasi2 = 0
while True:
    if count2 % 2:
        print(" "*spasi2,"+"*count2)
        spasi2 += 1
        count2 -=1
    else:
        count2 -= 1
        continue    

    #akan break jika count melebihi sisi
    if count2 < 1:
        break
    if spasi2 > sisi:
        break

