#Latihan date and time
import datetime as dt

print(10*"=","tanggal lahir",10*"=")
tanggal = int(input("Masukan tanggal lahir \t:"))
bulan = int(input("Masukan bulan lahir \t:"))
tahun = int(input("Masukan tahun lahir \t:"))
tanggal_lahir = dt.datetime(tahun,bulan,tanggal)
hari_ini = dt.date.today()
print(tanggal_lahir)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari lahir anda adalah : {tanggal_lahir:%A}")
umur = hari_ini.year - tanggal_lahir.year
bulan_lahir = hari_ini.month - tanggal_lahir.month
print(f"Umur anda sekarang adalah {umur} tahun {bulan_lahir} bulan ")