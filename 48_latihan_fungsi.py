'''latihan fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# membuat header program
#os.system("cls")

#print(f"{'PROGRAM KELILING LUAS':^40}")
#print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
#print(f"{'-'*40:^40}")


#mengambil input user

#LEBAR = int(input("Masukan nilai lebar : "))
#PANJANG = int(input("Masukan nilai panjang: "))

# Program menghitung luas

#LUAS = PANJANG*LEBAR
#KELILING = 2*(PANJANG+LEBAR)

#tampilkan hasilnya
#print(f"Hasil perhitungan luas = {LUAS}")
#print(f"Hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi header'''
    os.system("cls")
    print(f"{'PROGRAM KELILING LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    #mengambil input user
    '''input user'''

    lebar = int(input("Masukan nilai lebar : "))
    panjang = int(input("Masukan nilai panjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''hitung luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''hitung keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''
    print(f"Hasil perhitungan {message} = {value}")

#Program utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)
    
    display("luas", LUAS)
    display("keliling", KELILING)
    
    isContinue = input("Apakah lanjut (y/n)?")
    if isContinue == "n":
        break

print("Program selesai, terimakasih")