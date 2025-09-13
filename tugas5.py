# ========== function ===============

# fungsi sapaan
def greet(nama):
    print(f"Halo, {nama}!")


# fungsi penjumlahan
def tambah(a: float, b: float)-> float:
    return a + b


# fungsi rata - rata
def rata_rata(angka: list[float])-> float:
    n = len(angka)
    if not angka:
        return 0.0
    else:
        return sum(angka) / n 
    

# ========== CLASS ===============
class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float]):
        self.nama = nama
        self.nim = nim
        self.nilai = list(nilai)

    def tambah(self, skor):
        self.nilai.append(skor)
        
    def rata_rata(self):
        total = sum(self.nilai)
        return total / len(self.nilai)

    def status(self, rataRata: float, threshold: float = 70.0) -> str:
        if rataRata >= threshold:
            return "ANDA LULUS!"
        else:
            return "TIDAK LULUS"
        
    def __str__(self)->str:
        rata2 = self.rata_rata()
        status = self.status(rata2)
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={rata2:.1f}, status={status})"

if __name__ == "__main__":
    # === FUNCTIONS ===
    greet("arifian")
    print(tambah(5, 7)) 
    print(rata_rata([80, 90, 100]))
    print(rata_rata([]))
    # === CLASS ===
    joni = Student("Joni","F55123090",[91, 83, 75])
    print(joni)
    mellisa = Student("Melissa","F55123080",[99, 66, 57])
    print(mellisa)
    
    