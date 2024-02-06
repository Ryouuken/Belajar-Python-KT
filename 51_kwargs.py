import os

print(os.system("cls"))

'''**kwargs'''

print("===Fungsi Biasa===\n")
def fungsi(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",183,79)

print("\n===Fungsi Kwargs===\n")
def fungsi(**kwargs):
    '''fungsi kwargs'''
    print(kwargs)

fungsi(nama="ucup",tinggi=183,berat=90)

print("\n===Fungsi Kwargs yang lain===\n")
def fungsi(**kwargs):
    '''fungsi kwargs yang lain'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["tinggi"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup",tinggi=183,berat=90)

#studi kasus
print("\n===studi kasus kwargs dan args===\n")

def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka

    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka

    else:
        print("tidak ada operasi")
    return output

hasil= math(1,2,3,4,option="tambah")
print(f"hasil pertambahan adalah = {hasil}")

hasil= math(1,2,3,4,option="kali")
print(f"hasil perkalian adalah = {hasil}")