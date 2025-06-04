from metode_pembayaran import MetodePembayaran

class PembayaranKartuKredit(MetodePembayaran):
    def hitung_total(self, jumlah):
        biaya_tambahan = 0.03  
        return jumlah * (1 + biaya_tambahan)

    def bayar(self, jumlah):
        total = self.hitung_total(jumlah)
        print(f"\nMetode: Kartu Kredit\nBiaya tambahan: 3%\nTotal yang harus dibayar: Rp {total:.2f}")
