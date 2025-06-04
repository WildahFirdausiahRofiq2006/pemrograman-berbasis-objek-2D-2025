from kendaraan import Kendaraan

class Sepeda(Kendaraan):
    def proses_booking(self, usia):
        if usia < 12:
            print("Pemesanan sepeda gagal, usia minimal 12 tahun")
            return
        print("Booking sepeda berhasil.")

    def hitung_biaya(self):
        return 47000 

    def info_asuransi(self):
        return "Asuransi sepeda tidak tersedia"
