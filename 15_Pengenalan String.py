#membuat string

data = "ini string"
print(data)
print("data ini bertipe :", type(data))

## kita bisa membuat string dengan single quote dan double quote
print("\n===Single Quote & Double Quote===\n")
data = 'ini string dengan single quote'
print(data)
data = "ini string dengan double quote"
print(data)

##kita bisa membuat tanda ' menjadi string dengan menggunakan tanda \
print("\n===menggunakan tanda\ untuk menggadakan tanda '===\n")
data2 = 'sekarang hari jum\'at'
print(data2)
data2 = 'g\'day isn\'t it'
print(data2)

#Backslash (membuat backslash jadi terlihat dengan menggunakan double backslash)
print("\n===Backslash===\n")
print("C:\\User\\Ucup")

##tab \t (jadi jauh antara string satu dengan lainnya)
print("\n===tab===\n")
print("Ucup\tOtong, jadi jauhan")

#Backspace (menghilangkan satu karakter string , sama seperti hapus)
print("\n===Backslash===\n")
print("Ucup \bOtong, jadi deketan")

#newline(fungsinya mirip enter)
print("\n===Newline===\n")
print("Baris pertama.\nBaris kedua.") #-> LF ->Line feed -> Unix, Macos, Linux
print("Baris pertama.\rBaris kedua.") #->CR -> Carriage Return -> commodore,acorn, lisp
print("Baris pertama.\r\nBaris kedua.") #->CRLN -> Carriage Return Line Feed - > Windows

#String Literal atau Raw String
print("\n===Raw String===\n") 
# menggunakan r didepan tanda quote(jadi apapun yang didalamnya dianggap string)
print(r"C\new folder")

# multiline literal string , Menggunakan triple quote , jadi apa yang ada di dalamnya akan sama persis, termasuk enter nya

print("\n===multiline literal string===\n") 
print("""
Nama : Ucup
Kelas : 60 SD
""")

#Multiline Literal String dan RAW (jadi gabungan 2 diatas)
print("\n===multiline literal string===\n") 
print(r"""
Nama : Ucup
Kelas : 60 SD
Website : https:\\Ucup.com\NewID
""")