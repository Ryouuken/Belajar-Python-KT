friend = {
    "ucup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep penjual besek",
    "cuy" : "apa cuyyy"
}

# loop pertama (dia hanya mengambil key nya doang)
print("====Hanya key saja====")
for teman in friend:
    print(teman)

# loop kedua
#operator untuk mengambil item / iterables
print("\n====Key dan values (.keys)====")
keys = friend.keys()
print(keys)

for key in friend.keys():
    print(friend.get(key))

#Loop ketiga
print("\n====Values saja, (.values)====")
values = friend.values()
print(values)

for value in friend.values():
    print(value)

#loop keempat
print("\n====gabungan, (.items)====")
items = friend.items()
print(items)

for item in friend.items():
    print(item)

for key, value in friend.items():
    print(f"key = {key}, values = {value}")
