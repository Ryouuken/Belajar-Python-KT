class Crow:
    species = "bird"
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur= umur

ucup = Crow("Ucup", 15)
jajang = Crow("jajang", 26)

print("Ucup adalah = {}".format(ucup.__class__.species))
print("dan Jajang juga adalah = {}".format(jajang.__class__.species))

print("{} adalah {} tahun".format(ucup.nama, ucup.umur))
print("{} adalah {} tahun".format(jajang.nama, jajang.umur))