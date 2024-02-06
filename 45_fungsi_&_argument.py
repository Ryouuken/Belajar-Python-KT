'''membuat fungsi dengan argumennya'''

#fungsi string
def hello_world(nama):
    print(f"Selamat datang didunia wahai {nama}")

hello_world("Izan")
hello_world("Razan")



#fungsi tambah
def tambah(a,b):
    hasil = a + b
    print(f"{a} + {b} = {hasil}")


tambah(5,2)
tambah(1000,21002)

#fungsi list
def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup", "Otong", "Dudung"]

say_hi(anggota_boyband)