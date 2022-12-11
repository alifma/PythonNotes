# Integer (bilangan bulat)
data_integer = 1
print("data 1: ", data_integer)
print("- tipe: ", type(data_integer))

# Float (bilangan tak bulat, ada koma)
data_float = 1.25
print("data 2: ", data_float)
print("- tipe: ", type(data_float))

# String (Teks)
data_string = "User"
print("data 3: ", data_string)
print("- tipe: ", type(data_string))

# Boolean (True/False)
data_boolean = True
print("data 4: ", data_boolean)
print("- tipe: ", type(data_boolean))

# Complex (Bilangan Kompleks)
data_complex = complex(5, 6)
print("data 5: ", data_complex)
print("- tipe: ", type(data_complex))

# Bisa juga import tipe data dari C, karena python basenya dari c
from ctypes import c_double
data_c_double = c_double(1.25)
print("data 6: ", data_c_double)
print("- tipe: ", type(data_c_double))