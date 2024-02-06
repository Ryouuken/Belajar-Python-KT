'''fungsi dengan return'''

#fungsi kuadrat
print("\n===Fungsi kuadrat===\n")

def kuadrat(x):
    '''fungsi kuadrat'''
    output_kuadrat = x**2
    return output_kuadrat

y = kuadrat(3)
print(y)

# fungsi tambah
print("\n===Fungsi tambah===\n")

def fungsi_tambah(angka1, angka2):
    return angka1 + angka2

a = fungsi_tambah(10, 9)
print(a)

# fungsi dengan return banyak
print("\n===Fungsi return banyak===\n")

def operasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 / angka2
    bagi = angka1 * angka2

    return tambah, kurang, kali, bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil Tambah = {k}")
print(f"Hasil Kurang = {l}")
print(f"Hasil Kali = {m}")
print(f"Hasil Bagi = {n}")