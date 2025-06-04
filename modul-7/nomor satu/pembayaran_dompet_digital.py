from metode_pembayaran import MetodePembayaran

class PembayaranDompetDigital(MetodePembayaran):
    def hitung_total(self, jumlah):
        cashback = 1000  
        return max(0, jumlah - cashback)

    def bayar(self, jumlah):
        total = self.hitung_total(jumlah)
        print(f"\nMetode: Dompet Digital\nCashback: Rp 1000\nTotal yang harus dibayar: Rp {total:}")
