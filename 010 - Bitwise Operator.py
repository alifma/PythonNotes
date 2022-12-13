# Bitwise operator
# misal nilai a = 2 =  000000010
#       nilai b = 9 =  000001001

# Bitwise OR
# misal:
# - nilai_a = 1 = 000000001
# - nilai_b = 2 = 000000010
# hasilOr       = 000000011 / jadi di or kan masing-masing


# bitwise
a = 9
b = 5

c = a | b #OR, setidaknya salah satunya itu true
print("\n===============OR===============")
print("nilai ",a,",  binary :", format(a, '08b'))
print("nilai ",b,",  binary :", format(b, '08b'))
print("==============================(|)")
print("nilai ",c,", binary :", format(c, '08b'))

d = a & b #Keduanya harus true
print("\n==============AND===============")
print("nilai ",a,",  binary :", format(a, '08b'))
print("nilai ",b,",  binary :", format(b, '08b'))
print("==============================(&)")
print("nilai ",d,",  binary :", format(d, '08b'))

e = a ^ b #Exclusive or, harus salah satunya saja, jika keduanya maka salah
print("\n==============XOR===============")
print("nilai ",a,",  binary :", format(a, '08b'))
print("nilai ",b,",  binary :", format(b, '08b'))
print("==============================(^)")
print("nilai ",e,", binary :", format(e, '08b'))

f = ~a #di mirror di garis bilangan
print("\n==============NOT===============")
print("nilai ",a,",  binary :", format(a, '08b'))
print("==============================(~)")
print("nilai ",f,", binary :", format(f, '08b'))

g = a >> 1 #Shift right, geser ke kanan sebanyak binary
print("\n==========SHIFT RIGHT===========")
print("nilai ",a,",  binary :", format(a, '08b'))
print("==============================(>>)")
print("nilai ",g,", binary :", format(g, '08b'))

h = a << 1 #Shift left, geser ke kiri sebanyak binary
print("\n===========SHIFT LEFT===========")
print("nilai ",a,",  binary :", format(a, '08b'))
print("==============================(<<)")
print("nilai ",h,", binary :", format(h, '08b'))