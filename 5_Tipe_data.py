#tipe data angka satuan (Integer)
data_integer = 1
print("data :", data_integer, "bertipe :", type(data_integer))

#tipe data angka dengan koma (float)
data_float = 1.5
print("data :", data_float, "bertipe :", type(data_float))

#Tipe data string, kumpulan karakter
data_string = "si ucup"
print("data :", data_string, "bertipe :", type(data_string))

#Tipe data boolean, data biner atau true / false
data_boolean = True
print("data :", data_boolean, "bertipe :", type(data_boolean))

## tipe data khusus

#tipe data kompleks
data_complex = complex(5,6)
print("data :", data_complex, "bertipe :", type(data_complex))

#tipe data dari bahasa C
# jadi kita harus import dulu dari directory C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data :", data_c_double, "bertipe :", type(data_c_double))