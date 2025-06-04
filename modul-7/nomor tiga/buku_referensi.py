from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuReferensi(Peminjaman, Reservasi):
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.reservasi_oleh = None

    def info(self):
        return f"Buku Referensi: {self.judul} oleh {self.penulis}"

    def pinjam(self, nama):
        print("Buku referensi tidak bisa dipinjam.")

    def kembalikan(self):
        print("Buku referensi tidak sedang dipinjam karena tidak bisa dipinjam.")

    def reservasi(self, nama):
        if self.reservasi_oleh:
            print("Buku sudah dipesan.")
        else:
            self.reservasi_oleh = nama
            print(f"{nama} memesan buku referensi.")

    def batalkan_reservasi(self):
        if self.reservasi_oleh:
            print(f"Reservasi oleh {self.reservasi_oleh} dibatalkan.")
            self.reservasi_oleh = None
        else:
            print("Tidak ada reservasi aktif.")
