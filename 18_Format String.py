



#String
print("\n====String===\n")
nama = "ucup"
format_str = f"Hallo {nama}"
print(format_str)

#Boolean
print("\n====Boolean===\n")
boolean = True
format_str = f"Boolean = {boolean}"
print(format_str)

#Angka
print("\n====Angka===\n")
angka = 14.5
format_str = f"angka = {angka}"
print(format_str)

## Bilangan bulat (yang sebenrnya ga terlalu penting sih kalo bulat, pake yang atas lebih gampang)
print("\n====Angka Bulat===\n")
angka = 15
format_str = f"angka bulat = {angka:d}"
print(format_str) # jadi dia cuma bisa print angka bulat, kalo ada koma nya dia bakal error

## Angka dengan ordo ribuan (jadi di angkanya dikasih koma setiap ribuan, kayak 1,000 , 1,000,000)
print("\n====Angka ordo Ribuan===\n")
angka = 5000000
format_str = f"angka jutaan = {angka:,}"
print(format_str)

## Angka desimal (jadi kita bisa menentukan mau berapa angka dibelakang koma)
print("\n====Angka desimal===\n")
angka = 14.542564
format_str = f"angka = {angka:.2f}" # 2 disini artinya 2 angka dibelakang koma, f itu maksudnya float
print(format_str) # dan jangan lupa juga di {angka :} dikasih titik setelahnya yang artinya koma

## Angka leading Zero (jadi didepannya bisa dikasih 0)
print("\n====Angka Leading zero===\n")
angka = 14.542564
format_str = f"angka = {angka:07.2f}" # 7 disini artinya yang kita ambil hanya 5 string dari kiri (titik termasuk)
print(format_str) # jadi kalo mau diaksih 0 kita harus lebihin, terus dikasih 0 didepan angka itu

## Menampilkan tanda + atau - (kan biasanya si angka minus doang yang ada tandanya, ini si plus juga bakal ada)
print("\n====Angka Plus dan minus===\n")
angka_plus = 20
angka_minus = -30
format_plus = f"angka plus = {angka_plus:+d}" # jadi pake tanda :+ , plus ama minus sama aja tetep pake tanda +
format_minus = f"angka minus = {angka_minus:+d}" # ini pake d karena dia bilangan bulat, kalo desimal pake f

print(format_plus)
print(format_minus)

## Memformat %
print("\n====Memformat %===\n")
persentase = 0.033
format_persen = f"persen = {persentase:.1%}" # 1 disitu artinya mau berapa banyak angka debelakang koma
print(format_persen) # jangan lupa ya gais dikasih tanda . setelah titik dua

# Melakukan operasi aritmatika di placeholder
print("\n====Operasi aritmatika===\n")
harga = 10000
jumlah = 6
format_string = f"total harga = Rp. {harga*jumlah:,}" # tanda , setelah : itu untuk nanti hasilnya 
print(format_string) # setiap ribuan bakal dikasih tanda ,

# format angka lain (binary, octal, hexadecimal)
print("\n====Binary, Octal, Hex===\n")
angka = 255
format_binary = f"binary = {bin(angka)}" # jadi dikasih methods bin dahulu si angka nya
format_octal = f"octal = {oct(angka)}" # jadi dikasih methods oct dahulu si angka nya
format_hex = f"hex = {hex(angka)}" # jadi dikasih methods hex dahulu si angka nya

print(format_binary)
print(format_octal)
print(format_hex)