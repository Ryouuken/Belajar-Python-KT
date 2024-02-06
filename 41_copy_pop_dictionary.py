#copy dictionary

teman2 = {
    "cup": "ucup surucup",
    "tong": "otong surotong",
    "dung": "dudung surudung",
    "sep": "sep sepan",
    "cuy": "ucuy surucuy"
}

friends = teman2.copy()

#pop dictionary (jadi mengambil item di sebuah dicitonary) jadi di data sebelumnya akan menghilang, tapi hanya valuenya saja
dataasep = friends.pop("sep")
print(f"data asep = {dataasep}")
print(f"data friends = {friends}")

#pop item (mengambil data yang paling terakhir, key dan juga valuenya)

dataterakhir = friends.popitem()
print(f"data terakhir = {dataterakhir}")
print(f"data friends = {friends}")
