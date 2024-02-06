import datetime
# import os

# print(os.system("cls"))

data_waktu = datetime.datetime.now()

print(f"datetime now = {data_waktu}")
print(f"datetime now = {data_waktu.year}")
print(f"datetime now = {data_waktu.strftime('%A')}") # %A untuk menunjukan hari

from collections import Counter

data = ["a", "b", "c", "d", "d", "c", "a", "a", "b", "a"]

data_count = Counter(data)

print(f"data counter = {data_count}")
print(f"data a = {data_count['a']}")

import io

file = io.open("Kelas_terbuka_py/file_text.txt","r") # karena file_text.txt nya ada di dalem folder, jadi foldernya juga harus ditulis ulang terus dikasih "/"
print(file.read())

