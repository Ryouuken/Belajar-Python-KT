### casting meupakan merubah suatu tipe data ke tipe data yang lainnya
#begini contohnya , kita ubah data integer ke data lainnya , yaitu float, string dan boolean

#Integer
data_int = 9
print("data :", data_int, "bertipe :", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false bila data int = 0

print("data :", data_float, "bertipe :", type(data_float))
print("data :", data_str, "bertipe :", type(data_str))
print("data :", data_bool, "bertipe :", type(data_bool))

print("\n---------------------------------------\n")
#Float
data_float = 9.5
print("data :", data_float, "bertipe :", type(data_float))

data_int = int(data_float) # akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false bila data float = 0

print("data :", data_int, "bertipe :", type(data_int))
print("data :", data_str, "bertipe :", type(data_str))
print("data :", data_bool, "bertipe :", type(data_bool))

print("\n---------------------------------------\n")
#boolean

data_bool = True
print("data :", data_bool, "bertipe :", type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool) 

print("data :", data_int, "bertipe :", type(data_int))
print("data :", data_str, "bertipe :", type(data_str))
print("data :", data_float, "bertipe :", type(data_float))

print("\n---------------------------------------\n")

#string

data_str = "9"
print("data :", data_str, "bertipe :", type(data_str))

data_int = int(data_str) #string harus angka
data_float = float(data_str) #string harus angka
data_bool = bool(data_str) #false jika string kosong (tidak ada isinya)

print("data :", data_int, "bertipe :", type(data_int))
print("data :", data_float, "bertipe :", type(data_float))
print("data :", data_bool, "bertipe :", type(data_bool))
