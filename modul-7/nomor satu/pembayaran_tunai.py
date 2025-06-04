from metode_pembayaran import MetodePembayaran

class PembayaranTunai(MetodePembayaran):
    def hitung_total(self, jumlah):
        diskon = 0.05  
        return jumlah * (1 - diskon)

    def bayar(self, jumlah):
        total = self.hitung_total(jumlah)
        print(f"\nMetode: Tunai\nDiskon: 5%\nTotal yang harus dibayar: Rp {total:.2f}")
