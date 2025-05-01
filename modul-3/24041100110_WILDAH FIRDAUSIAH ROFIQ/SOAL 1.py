class Karyawan:
    def __init__(self,nama,gaji,departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def Info(self):
        print(f"Nama : {self.nama}")
        print(f"Gaji : {self.gaji}")
        print(f"Departemen : {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji,departemen, tunjangan):
        Karyawan.__init__(self, nama, gaji, departemen)
        self.tunjangan = tunjangan

    def Info(self):
        Karyawan.Info(self)
        print(f"Tunjangan : {self.tunjangan}")
        print(f"Status Karyawan Tetap\n")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, tambahan_jam_kerja):
        Karyawan.__init__(self, nama, gaji, departemen)
        self.tambahan_jam_kerja = tambahan_jam_kerja

    def Info(self):
        Karyawan.Info(self)
        print(f"Jam kerja per harinya: {self.tambahan_jam_kerja}")
        print(f"Status Karyawan Harian\n")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)
    
    def tampilkan_semua_karyawan(self):
        print(f"==== DAFTAR SEMUA KARYAWAN ====")
        for karyawan in self.daftar_karyawan:
            karyawan.Info()

manajemen = ManajemenKaryawan()

while True:
    print("\n=== MENU TAMBAH KARYAWAN ===")
    tipe = input("Masukkan tipe karyawan (tetap/harian): ")

    nama = input("Nama: ")
    gaji = int(input("Gaji: "))
    departemen = input("Departemen: ")

    if tipe == "tetap":
        tunjangan = int(input("Tunjangan: "))
        karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
    elif tipe == "harian":
        jam_kerja = int(input("Jam kerja per hari: "))
        karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
    else:
        print("Tipe karyawan tidak dikenali. Coba lagi.")
        continue

    manajemen.tambah_karyawan(karyawan)

    lagi = input("Tambah karyawan lagi? (ya/tidak): ")
    if lagi != 'ya':
        break

manajemen.tampilkan_semua_karyawan()
