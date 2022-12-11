#Casting
# Mengubah tipe data ke tipe data lainnya

print("================INTEGER=================")
data = 10
data_float = float(data)
data_str = str(data)
data_bool = bool(data) #  false kalau 0
print("data = ", data, ", type=", type(data))
print("data = ", data_float, ", type=", type(data_float))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_bool, ", type=", type(data_bool))

print("================FLOAT=================")
data = 9.9
data_int = int(data) # Pembulatan ke bawah
data_str = str(data)
data_bool = bool(data) #  false kalau 0
print("data = ", data, ", type=", type(data))
print("data = ", data_int, ", type=", type(data_int))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_bool, ", type=", type(data_bool))

print("================BOOLEAN=================")
data = True
data_int = int(data)
data_float = float(data)
data_str = str(data)
print("data = ", data, ", type=", type(data))
print("data = ", data_int, ", type=", type(data_int))
print("data = ", data_float, ", type=", type(data_float))
print("data = ", data_str, ", type=", type(data_str))

print("================STRING=================")
data = "0"
data_int = int(data)
data_float = float(data)
data_bool = bool(data) # false kalau stringnya kosong
print("data = ", data, ", type=", type(data))
print("data = ", data_int, ", type=", type(data_int))
print("data = ", data_float, ", type=", type(data_float))
print("data = ", data_bool, ", type=", type(data_bool))