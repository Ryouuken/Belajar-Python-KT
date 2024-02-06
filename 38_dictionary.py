# List itu -> Array
print("====List====")
## Menggunakan Index

data_list = ["ucup", "otong", "dudung"]

print(data_list)
print(data_list[0])

# Dictionary -> Associate Array
print("====Dictionary====")

data_dict = {
    "key": "value",
    "cp" : "ucup",
    "tg" : "otong",
    "dg" : "dudung",
    "nmbr" : 100,
    "list" : data_list
}

print(data_dict["key"])
print(data_dict["tg"])
print(data_dict["nmbr"])
print(data_dict["list"])

## jadi bahkan didalam dictionary kita bisa memasukan list lagi, atau bahkan dictionary lagi pun bisa