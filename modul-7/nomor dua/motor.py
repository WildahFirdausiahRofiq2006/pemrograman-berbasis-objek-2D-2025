from kendaraan import Kendaraan

class Motor(Kendaraan):
    def proses_booking(self, usia):
        if usia < 17:
            print("Pemesanan motor gagal, usia minimal 17 tahun")
            return
        print("Booking motor berhasil.")

    def hitung_biaya(self):
        return 185000  

    def info_asuransi(self):
        return "Asuransi motor hanya untuk kerusakan ringan"
