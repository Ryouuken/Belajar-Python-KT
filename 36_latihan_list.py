#membuat direktori buku

list_buku = []

while True:
    print("\n Masukan Data Buku:")
    judul = input("Masukan Judul\t:")
    penulis = input("Masukan Nama Penulis: \t")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n=====Data Buku=====")
    for index,buku in enumerate(list_buku):
        print(f"{index + 1} | {buku[0]} | {buku[1]}")

    print("="*20)
    lanjut = input("Apakah mau lanjut? y/n")
    if lanjut == "n":
        break

print("Program Selesai")