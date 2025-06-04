from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        
        self.peminjam = None
        self.reservasi_oleh = None

    def info(self):
        return f"Buku Fiksi: {self.judul} oleh {self.penulis}"

    def pinjam(self, nama):
        if self.peminjam:
            print("Buku sudah dipinjam.")
        else:
            self.peminjam = nama
            print(f"{nama} meminjam buku ini.")

    def kembalikan(self):
        if self.peminjam:
            print(f"{self.peminjam} mengembalikan buku.")
            self.peminjam = None
        else:
            print("Buku tidak sedang dipinjam.")

    def reservasi(self, nama):
        if self.reservasi_oleh:
            print("Buku sudah dipesan.")
        else:
            self.reservasi_oleh = nama
            print(f"{nama} memesan buku ini.")

    def batalkan_reservasi(self):
        if self.reservasi_oleh:
            print(f"Reservasi oleh {self.reservasi_oleh} dibatalkan.")
            self.reservasi_oleh = None
        else:
            print("Tidak ada reservasi yang aktif.")
