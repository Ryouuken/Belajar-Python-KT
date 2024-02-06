import ipa
from ipa.matematika import scientific

hasil_tambah = ipa.matematika.tambah(1,2,3,4,5)

print(f"hasil tambah = {hasil_tambah}")

gaya = ipa.fisika.gaya(10,5)

print(f"hasil gaya = {gaya}")

hasil_kali = ipa.matematika.kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

hasil_pangkat = scientific.pangkat(3)
print(f"hasil pangkat = {hasil_pangkat(5)}")