from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_pokok):
        super().__init__(nama)
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, jam_kerja, upah_per_jam):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.upah_per_jam

def cetak_gaji(karyawan):
    print(f"\nNama: {karyawan.nama}")
    print(f"Gaji: Rp{karyawan.hitung_gaji():,.2f}")

def main():
    daftar_karyawan = []

    while True:
        print("\n=== Input Data Karyawan ===")
        nama = input("Masukkan nama karyawan: ")
        tipe = input("Jenis karyawan (tetap/kontrak): ").lower()

        if tipe == "tetap":
            gaji_pokok = float(input("Masukkan gaji pokok: "))
            karyawan = KaryawanTetap(nama, gaji_pokok)
        elif tipe == "kontrak":
            jam_kerja = float(input("Masukkan total jam kerja: "))
            upah_per_jam = float(input("Masukkan upah per jam: "))
            karyawan = KaryawanKontrak(nama, jam_kerja, upah_per_jam)
        else:
            print("Jenis karyawan tidak valid. Ulangi.")
            continue

        daftar_karyawan.append(karyawan)

        lanjut = input("Tambah karyawan lagi? (ya/tidak): ").lower()
        if lanjut != 'ya':
            break

    print("\n=== Daftar Gaji Karyawan ===")
    for k in daftar_karyawan:  
        cetak_gaji(k)

main()
