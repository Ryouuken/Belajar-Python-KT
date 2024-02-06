import numpy as np

# dengan numpy dan .array bisa melakukan operasi mtk pada list
# karena untuk .array dia pakai list
vector_a = np.array([1,2,3,4])

print(f"vektor a = {vector_a}")
print(f"vektor a = {vector_a**2}")
print(f"vektor a = {vector_a*5}")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b = \n{matrix_b**2}")

# cara membuat matrix yang berisi 0 semua

zeros_c = np.zeros((2,2))
#(2,2) itu adalah dimensi si list nya nanti
print(f"zeroc c = \n{zeros_c}")

# cara membuat matrix yang berisi 1 semua
ones_d = np.ones((2,2))
#(2,2) itu adalah dimensi si list nya nanti
print(f"ones d = \n{ones_d}")

# dengan numpy kita bisa juga melakukan operasi matematika
# dengan sesama matrix, contohnya kita tambah matrix b dengan ones

jumlah = matrix_b + ones_d 
print(f"jumlah = {jumlah}")
# tetapi harus yang bentuknya sama ya, kan yang matrix b sama vector a
# itu beda bentuknya, si vector a dia satu list, sedangkan si matrix b
# dia 2 list jadi ga bisa dijumlahkan