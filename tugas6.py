import numpy as np
import pandas as pd
import os


nilaiNumpy = np.array([80, 97, 78, 90, 100, 77, 89, 91, 88, 88], dtype=np.uint32) # dtype ini cmn sy tetapkan tipe datanya saja
# rata- rata
rata_rata = sum(nilaiNumpy) / len(nilaiNumpy)


# median
median = np.median(nilaiNumpy)


# standard deviasi
std = np.std(nilaiNumpy)

# min dan max
def nilai_min(data):
    if len(data) == 0: # tidak bisa pake if not data, karena bukan list dipakai kasusnya, ini menggunakan numpy nddaray
        return "Data Anda Tidak Ada!"
    terkecil = data[0] # karena mulainya juga dari data[0] untuk pengecekkan
    for i in range(1 , len(data)): 
        if data[i] < terkecil  :
            terkecil = data[i]
    return terkecil
    


def nilai_max(data):
    if len(data) == 0:
        return "Data Anda Tidak Ada!"
    terbesar = data[0] 
    for i in range(1 , len(data)): # range bisa simpan 2 parameter, yang pertama itu artinya mulai dari indeks ke-1
        if data[i] > terbesar :
            terbesar = data[i]
    return terbesar



# data frame
df= pd.DataFrame(
    {
        "nama":"Mohammad Raiyan",
        "NIM": "F55123001",
        "Nilai": np.array([70, 88, 77, 85, 95])
    }
)
df = df.assign(status="TIDAK LULUS") # untuk assign kolom baru menggunakan "assign()" tidak perlu dibungkus dalam kutip 2 !
df.loc[df['Nilai'] >= 70, "status"] = "LULUS" # loc = loc itu fitur di pandas untuk mengambil/menetapkan baris & kolom 
#berdasarkan nama label (bukan nomor urut), atau memakai filter boolean.
# ==> loc[baris, kolom] <== (baris itu bisa nama index, irisan label, atau kondisi boolean)
# file input / output
dataString = df.to_string()

# Menulis sesuatu yang baru ke file
with open('ringkasan_tugas6.txt', 'w') as file:
  file.write(dataString)

# OOP SEDERHANA
class GradeBook:
    def __init__(self, df: pd.DataFrame):
            self.df = df
    
    def average(self)->float:
        return sum(self.df["Nilai"]) / len(self.df["Nilai"])
    
    # menampilkan presentase
    def pass_rate(self, threshold: float = 70.0) -> float:
        n_nilai = len(self.df)
        if n_nilai == 0:
            return 0.0
        
        lulus = (self.df["Nilai"] >= threshold).sum()
        return 100 * lulus/n_nilai
    def __str__(self)->str:
        return f"GradeBook(n_nilai={len(self.df)}, avg={self.average():.2f}, pass_rate={self.pass_rate():.1f}%)"

# DEMO
if __name__ == "__main__":
    print("\n=== NUMPY ===")
    print(rata_rata)
    print(median)
    print(std)
    
    # pake fungsi buatan
    print(nilai_max(nilaiNumpy))
    print(nilai_min(nilaiNumpy))
    print("\n")
    # numpy min max
    print("\nPAKE NUMPY MIN MAX")
    print(nilaiNumpy.min())
    print(nilaiNumpy.max())
    
    print("=== PANDAS ===")
    print(df.head())
    print("\n")
    
    print("=== OOP: GRADEBOOK ===")
    objekGradeBook = GradeBook(df)
    print(objekGradeBook)
    print("Average (df):", objekGradeBook.average())
    print("Pass rate   :", f"{objekGradeBook.pass_rate():.1f}%")
    
    