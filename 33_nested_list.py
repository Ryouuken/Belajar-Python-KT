#contoh penggunaan 

peserta_0 = ["Ucup", 10, "Laki-laki"]
peserta_1 = ["Otong", 12, "Laki-laki"]
peserta_2 = ["Leha", 18, "Perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"Pesertanya adalah = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t : {peserta[0]}")
    print(f"Umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")

#dengan reference

list_copy = list_peserta.copy()
print(f"peserta : {list_copy}")
peserta_0[0] = "Michael"
print(f"peserta : {list_copy}")
print(f"Pesertanya adalah = {list_peserta}")

## bisa dilihat bahwa padahal sudah pake .copy() tapi masih berubah juga, untuk penjelasannya kenapa begitu
## akan diberitahu di pembahasan selanjutnya