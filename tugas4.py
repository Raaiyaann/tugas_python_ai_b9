

data = ["Raiyan", 27, 3.14, False, "Informatika", 0, 2.718, True]
print(f"Nilai Elemen Pertama: {data[0:1]}")
print(f"Nilai Elemen Terakhir {data[7:8]}")

data.append(False)
print(data)
data.insert(4, "Teknik")
print(data)
data.pop(-2) # menghapus true
print(data)
data.remove(27)
print(data)
print("\n")

# ini untuk extend
cars = ["bmw", "volvo", "avanza"]
data.extend(cars)
print(data)
print("\n")

# =========== TUPLE =================
dataTuple = ("Roni", "Raiyan", "Samantha", "Bobby", "Adit")
print(f"Panjang Tuple: {len(dataTuple)}")
print(f"Nama Siswa Indeks Ke 3: {dataTuple[3]}")
siswa1, siswa2, *siswaYangLain = dataTuple
print(siswa1) # siswa pertama
print(siswa2) # siswa kedua
print(siswaYangLain) # sisa siswa

# =========== LIST =================
set_a = {2, 3, 5, 7, 11}
set_b = {5, 7, 11, 13, 17}

irisan = set_a.intersection(set_b)
print(irisan)
gabungan = set_a.union(set_b)
print(gabungan)
selisih = set_a.difference(set_b) # ini menampilkan yang ada di A tapi tidak ada di B
print(selisih)
beda_setangkup = set_a.symmetric_difference(set_b) # menampilkan yang ada di A tidak ada di B, dan yang ada di B tidak ada di A
print(beda_setangkup)

# =========== DICITIONARY =================
dataMahasiswa = {
    "Nama": "Mohammad Raiyan",
    "NIM": "F55123001",
    "Angkatan": 2023,
    "Kota": "Palu"
}

dataMahasiswa["hobi"] = "Main Gitar"
print(dataMahasiswa) 
dataMahasiswa["NIM"] = "F55123123"
print(f"Data Setelah Diubah: {dataMahasiswa}")
del dataMahasiswa["Kota"]
print(f"Data Setelah Dihapus: {dataMahasiswa}\n")

# menampilkan values dan keysnya
print(dataMahasiswa.keys())
print(dataMahasiswa.values())
print(dataMahasiswa.items())
for key in dataMahasiswa: # dictionary itu tidak mengambil angka indeks menggunakan length() begitu, tapi langsung mengambil keynya dan akses valuesnya itu namaKey[value]
    print(key,":",dataMahasiswa[key])
print("\n")

# =========== Nested Structures =================
buku = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
    {"judul": "Filosofi Kopi", "penulis": "Dewi Lestari", "tahun": 2006},
    {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "tahun": 2009},
    {"judul": "Bumi", "penulis": "Tere Liye", "tahun": 2014},
    {"judul": "Hujan", "penulis": "Tere Liye", "tahun": 2016},
]

for indeksBuku in range(len(buku)):
    print(buku[indeksBuku])
    
print("\n")
# list comprehension
filterBuku = []
filterBuku = [bukuTahunTerbitFilter for bukuTahunTerbitFilter in buku if bukuTahunTerbitFilter["tahun"] >= 2009]

# dibawah ini alternative dari menggunakan list comprehension, agar bisa terbayang cara kerjanya list comprehension itu sama saja seperti dibawah ini

# for bukuTahunTerbitFilter in buku:
#     if bukuTahunTerbitFilter["tahun"] >= 2009:
#         filterBuku.append(bukuTahunTerbitFilter)
    
print(filterBuku) # ini akan menyimpan judul buku yang keluaran tahun diatas 2009 dan 2009 itu sendiri
print("\n")
# =========== Comprehension Dan Utilitas =================
# ============ LIST COMPREHENSION ===================
listAngka = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
angkaGenap = []
hasilAngkaKuadrat = []
angkaGenap = [digitGenap for digitGenap in listAngka if digitGenap % 2 == 0]
print(angkaGenap)

# algorimat tanpa menggunakan library math untuk filter angka kuadrat
# kalau misalkan elemen angkanya hanya sampai 20, berarti hanya terdapat 1^2, 2^2, 3^2, 4^2
max_n = max(x for x in listAngka if x >= 0)
print(max_n) # berarti max_n ini hanya mengambil nilai terbesar dari list, yaitu 20
k = 0
angkaKuadrat = set() # kalau mau definisikan variabel jadi set itu harus pake fungsi set(), kalau diisi dengan nilai "{}", nanti dibacanya dictionary
while k*k <= max_n:
    angkaKuadrat.add(k*k)
    k += 1
hasilAngkaKuadrat = [x for x in listAngka if x in angkaKuadrat]
print(f"Nilai-Nilai Yang Masuk Dalam Kategori Kuadrat: {hasilAngkaKuadrat}\n")

# ============ Dict Comprehension ===================

listAngka2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listJenisAngka = ["ganjil", "genap"]

dictAngka = {
        listJenisAngka[0] : [x for x in listAngka2 if x % 2 == 1],
        listJenisAngka[1] : [x for x in listAngka2 if x % 2 == 0]
}
print(dictAngka)

# ============ SET COMPREHENSION ===================

setsWarna = {"BIRU", "HIJAU", "MERAH", "KUNING", "UNGU"}
# cara 1: untuk validasi tipe data setnya string semua
# lowerCase_set = {item.lower() for item in setsWarna if isinstance(item, str)} # isintance mengembalikan boolean, artinya jika nilai item string, maka true kalau bukan maka jadi false
# # berarti diatas itu True string nilainya, maka akan dimasukan ke item dan di lowercase() itemnya

# cara 2:
lowerCase_set = {x.lower() for x in setsWarna} # bisa juga pake ini jika yakin nilai setnya itu string semua tipe datanya
print(lowerCase_set)

# ini untuk kalimat text:
unique_words = set()

text = """
 Beautiful is better than ugly
 Explicit is better than implicit
 Simple is better than complex
 Complex is better than complicated
 """.lower()

print(text.strip())
print("\n")

# ============ KENAGOTAAN DAN PENCARIAN SEDERHANA ===================
angka_list = [10, 20, 30, 20]
angka_set  = {10, 20, 30}

print(20 in angka_list)  # True karena ada angka 20
print(40 in angka_list)  # False karena tidak ada angka 40

if 30 in angka_list:
    print(f"Angka 30 terdapat pada index ke: {angka_list.index(30)}")
else:
    print("angka 30 tidak ada")
    

