class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan
    
    def estimasi_waktu(self):
        return 5 

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
    
    def estimasi_waktu(self):
        if self.jenis_kendaraan == "Kereta Api":
            return 4  
        elif self.jenis_kendaraan == "Truk":
            return 6  
        else:
            return 7  
        
class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
    
    def estimasi_waktu(self):
        if self.maskapai == "Garuda Indonesia":
            return 2  
        elif self.maskapai == "Citilink":
            return 3  
        else:
            return 4  

class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan=None, maskapai=None):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai
    
    def estimasi_waktu(self):
        if self.tujuan == "Luar Negeri":
            if self.jenis_kendaraan:
                waktu_estimasi = PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan).estimasi_waktu()
            elif self.maskapai:
                waktu_estimasi = PengirimanUdara(self.asal, self.tujuan, self.maskapai).estimasi_waktu()
            return waktu_estimasi + 3  
        else:
            if self.jenis_kendaraan:
                return PengirimanDarat(self.asal, self.tujuan, self.jenis_kendaraan).estimasi_waktu()
            elif self.maskapai:
                return PengirimanUdara(self.asal, self.tujuan, self.maskapai).estimasi_waktu()
            return 0  

daftar_pengiriman = []

while True:
    print("\n=== Input Pengiriman ===")
    asal = input("Asal pengiriman: ")
    tujuan = input("Tujuan pengiriman (dalam negeri / luar negeri): ")
    
    metode = input("Metode pengiriman (darat / udara): ")
    
    if metode == "darat":
        kendaraan = input("Jenis kendaraan (kereta api / truk / lainnya): ")
        pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan=kendaraan)
    elif metode == "udara":
        maskapai = input("Maskapai (garuda indonesia / citilink / lainnya): ")
        pengiriman = PengirimanInternasional(asal, tujuan, maskapai=maskapai)
    else:
        print("Metode tidak valid. Coba lagi.")
        continue

    daftar_pengiriman.append(pengiriman)

    lagi = input("Tambah data pengiriman lagi? (ya/tidak): ")
    if lagi != 'ya':
        break

print("\n=== Estimasi Waktu Pengiriman ===")
i = 1 
for p in daftar_pengiriman:
    print(f"Pengiriman {i}: Estimasi waktu = {p.estimasi_waktu()} hari")
    i += 1  
    # ..