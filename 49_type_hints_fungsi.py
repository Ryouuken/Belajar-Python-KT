import os
import string

# intinya type hints fungsinya adalah untuk memberi tau kepada
# pembaca kode selanjutnya bahwa untuk mengisi parameternya
# memerlukan type apa, entah itu int,string,boolean atau apapun  
''' type hint untuk fungsi'''

#bentuk standar fungsi yang sudah dipelajari

'''
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

 fungsi(1)
 fungsi("ucup")
'''


print(os.system("cls"))
#penggunaan type hints

def sepuluh_pangkat(argument:int) -> int:
    hasil = 10**argument
    return hasil

HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument:string):
    print(argument)

display("ucup")

