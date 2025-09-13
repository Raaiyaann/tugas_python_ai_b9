nama = "Mohammad Raiyan"
umur = 20
tinggi = 161.3
isMarried = False
hobby = ["sport", "musik", "gaming", "berenang", "baca Buku"]

print(len(nama))
print(nama.upper())
print(nama.lower())
print("\n")

# operasi matematika
a = 12
b = 8
penjumlahan = a + b
perkalian = a * b
pembagian = a / b
pembagianSisa = a % b
pembagianBulat = a // b

print(f"hasil penjumlahan: {penjumlahan}")
print(f"hasil perkalian: {perkalian}")
print(f"hasil pembagian: {pembagian}")
print(f"hasil pembagian Sisa: {pembagianSisa}")
print(f"hasil pembagian Bulat: {pembagianBulat}\n")

# akses hobby list
print(f"Salah Satu Hobi Saya Adalah: {hobby[2]}")
hobby.append("Makan")
hobby.remove("berenang")
hobby.pop(-3) # mengahpus gaming karena -3 itu dihitung dari belakang indeksnya
print(hobby)
print("\n")

# memasukan input nama dan umur
nama = input("Silahkan Masukan Nama Anda: ")
umur = input("Silahkan Masukan Umur Anda: ")
print(f"Hallo, Nama saya {nama} dan umur saya {umur}")
