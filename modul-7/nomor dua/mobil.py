from kendaraan import Kendaraan

class Mobil(Kendaraan):
    def proses_booking(self, usia):
        if usia < 21:
            print("Pemesanan mobil gagal, usia minimal 21 tahun")
            return
        print("Booking mobil berhasil.")

    def hitung_biaya(self):
        return 480000  

    def info_asuransi(self):
        return "Asuransi mobil untuk kerusakan dan kecelakaan"
