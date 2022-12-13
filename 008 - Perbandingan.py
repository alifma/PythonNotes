# Operasi Logika
# Equal
x = 1
y = 2
z = 1
# Equal: Bandingin nilai apakah valuenya sama
hasilEqual = x == y
# Not Equal: Kebalikan dari equal
hasilNotEqual = x != y
# Less Than: Apakah nilai kiri lebih kecil dari nilai kanan?
hasilLessThan = x < y
# Less Than Equal: Apakah nilai kiri lebih kecil atau sama dengan nilai kanan?
hasilLessThanEqual = x <= y
# More Than: Apakah nilai kiri lebih besar dari nilai kanan?
hasilMoreThan = x > y
# More Than Eqal: Apakah nilai kiri lebih besar atau sama dengan nilai kanan?
hasilMoreThanEqual = x >= y
# And: Membandingkan apakah keduanya itu true
hasilAnd = x and y
# Or: Membandingkan apakah salah satunya ada yang true
hasilOr  = x or y
# Not: Kebalikan dari nilai yang diminta (selain)
hasilNot = not (x and y)
# Is: Membandingkan apakah nilai dalam dua memori ini sama?, tidak bisa literal diketik, harus ke arah variable
hasilIs = x is z


print("Comparison Operator:")
print("- Equal         (==) :", hasilEqual)
print("- Not Equal     (!=) :", hasilNotEqual)
print("- Less          (<)  :", hasilLessThan)
print("- Less or Equal (<=) :", hasilLessThanEqual)
print("- More          (>)  :", hasilMoreThan)
print("- More or Equal (>=) :", hasilMoreThanEqual)
print("")
print("Logical Operator   :")
print("- Equal         (and):", hasilEqual)
print("- Or            (or) :", hasilOr)
print("- Not           (not):", hasilNot)
print("")
print("Special:")
print("- Is            (is):", hasilIs)