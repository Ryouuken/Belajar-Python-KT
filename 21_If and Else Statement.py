nama = input("Masukan nama anda :")

#1. program if inline
print("====if inline====")

if nama == "hafiz" : print("kamu keren abiiieezzz")

#2. program if indentation, jadi setelah titik 2 dia di enter tapi kayak ada tabnya gitu menjorok kedalam
print("====if indentation====")

if nama == "hafiz" :
    print("kamu keren abiiiezzz")
    print("kamu juga kece abiieezzz")
print(f"Terimakasih {nama}")

#3. program ELSE
print("====ELSE====")
if nama == "hafiz" :
    print("wah kamu keren banget bang")
else:
    print("halah kamu bukan hafiz, kamu tidak keren")
print("akhir dari program")