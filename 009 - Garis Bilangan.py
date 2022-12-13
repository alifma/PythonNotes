# Garis bilangan
# Latihan kondisi dengan menggunakan garis bilangan
#  +++++++++++++3-----------7+++++++++++++
#  Kurang dari sama dengan 3 maka true, lebih dari sama dengan 7 maka true,
# antara 3 dan 7 maka false

def GarisBilangan():
  rangeBawah = 3
  rangeAtas = 7
  print("===============|Aplikasi Garis Bilangan|==============")
  inputUser = int(input("Masukkan angka antara "+str(rangeBawah)+" sampai "+str(rangeAtas)+": "))

  lessThan = inputUser <= rangeBawah
  moreThan = inputUser >= rangeAtas
  between = rangeBawah < inputUser and inputUser < rangeAtas 

  print(str(inputUser)+" kurang dari "+str(rangeBawah)+": "+str(lessThan))
  print(str(inputUser)+" lebih dari "+str(rangeAtas)+": "+str(moreThan))
  print(str(inputUser)+" antara "+str(rangeBawah)+" dan "+str(rangeAtas)+": "+str(between))

GarisBilangan();