def konversiSuhu():
# Program konversi suhu

  print("================|APLIKASI KONVERSI SUHU|==============")
  # Mengambil input untuk suhu awal, suhu akhir, dan suhunya
  suhuInput = float(input("Masukkan suhu awal                  : "))
  suhuAwal  =      input("Masukkan jenis suhu input (C/R/F/K) : ")
  suhuAkhir =      input("Masukkan jenis suhu output (C/R/F/K): ")
  result    = float(0)

  celcius  = float(0)

  # Konversi dari nilai input ke celcius
  if suhuAwal == "C":
    celcius = suhuInput
  elif suhuAwal == "R":
    celcius = (4/5)*suhuInput
  elif suhuAwal == "F":
    celcius = (5/9)*(suhuInput-float(32))
  elif suhuAwal == "K":
    celcius = suhuInput-273
  else:
    print("Error: Invalid input type")
    return

  # Konversi dari nilai celcius ke nilai tujuan
  if suhuAkhir == "C":
    result = celcius
  elif suhuAkhir == "R":
    result = (4/5)*celcius
  elif suhuAkhir == "F":
    result = ((9/5)*celcius)+float(32)
  elif suhuAkhir == "K":
    result = celcius + float(273)
  else:
    print("Error: Invalid output type")
    return

  print("Hasil perhitungan: ")
  print("- Data input : ", suhuInput,suhuAwal)
  print("- Data Output: ", result,suhuAkhir)
  return
    
konversiSuhu()