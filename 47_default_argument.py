'''default argument'''

# def fungsi (argument):
# def fungsi(argument = nilai default):

#contoh 1
def say_hello(nama):
    '''fungsi tanpa default argument'''
    print(f"Halo {nama}")

say_hello("ucup")


def say_hello2(nama = " Ganteng"):
    '''fungsi dengan default argument'''
    print(f"Halo{nama}")

say_hello2()

#contoh 2
def sapa_dia(nama, pesan = "Apa kabar"):
    print(f"Hai {nama}, {pesan}")

sapa_dia("Ucup", "Ma friend")
sapa_dia("Maman")

#contoh 3
def hitung_pangkat(angka, pangkat=5):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(5, 3))
print(hitung_pangkat(2))

#contoh 4
def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=5))