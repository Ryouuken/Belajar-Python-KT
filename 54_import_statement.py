import os

print(os.system("cls"))

#import

# fungsinya adlah untuk mengambil program dari file external .py
# jadi tuntuk latihan kali ini 
# bikin dulu file nya, baru di import
# bisa juga sih pake bawaan python, cuma kali ini
# kita akan buat sendiri 

# 1. untuk menyambung program

import program_print

#2. import dengan data
import variable

print(variable.data)

#3 3. import dengan fungsi
import matematika
hasil = matematika.tambah(4,5)

print(hasil)