class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.validasi_sks(sks):
            print(f"SKS untuk {nama} tidak valid! Harus 2 atau 3.")
            self.valid = False
        else:
            self.valid = True
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in (2, 3)

    def __str__(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"

class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            print(f"NIM {nim} tidak valid! Harus dimulai dengan '23' dan panjang 10 digit.")
            self.valid = False
        else:
            self.valid = True
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_biodata(self):
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for mk in self.matkul_diambil:
            print(f"  - {mk}")

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10


class Kampus:
    total_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            print(f"Nama kampus '{nama}' tidak valid! Tidak boleh mengandung angka.")
            self.valid = False
        else:
            self.valid = True
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info_kampus(cls, nama):
        print(f"\nNama Kampus: {nama}")
        print(f"Total Mahasiswa Terdaftar: {cls.total_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)


# Input data kampus
print("=== Input Data Kampus ===")
nama_kampus = input("Nama Kampus: ")
alamat_kampus = input("Alamat Kampus: ")
kampus = Kampus(nama_kampus, alamat_kampus)

# Input mata kuliah
print("\n=== Input 8 Mata Kuliah ===")
daftar_matkul = {}
for i in range(8):
    print(f"\nMata Kuliah ke-{i+1}")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks = int(input("SKS (2 atau 3): "))
    matkul = MataKuliah(kode, nama, sks)
    if matkul.valid:
        daftar_matkul[kode] = matkul

# Input mahasiswa
print("\n=== Input 6 Mahasiswa ===")
daftar_mahasiswa = []
for i in range(6):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")
    nim = input("NIM: ")
    prodi = input("Prodi: ")
    mhs = Mahasiswa(nama, nim, prodi)
    if not mhs.valid:
        continue

    print("\nPilih 4 kode mata kuliah yang ingin diambil:")
    for k in daftar_matkul:
        print(f"  {daftar_matkul[k]}")

    dipilih = set()
    while len(dipilih) < 4:
        kode = input(f"Kode matkul ke-{len(dipilih)+1}: ")
        if kode in daftar_matkul and kode not in dipilih:
            mhs.tambah_matkul(daftar_matkul[kode])
            dipilih.add(kode)
        else:
            print("Kode tidak ditemukan atau sudah dipilih.")

    daftar_mahasiswa.append(mhs)
    Kampus.total_mahasiswa += 1

# Output data
print("\n========== DATA MAHASISWA ==========")
for m in daftar_mahasiswa:
    m.tampilkan_biodata()

Mahasiswa.tampilkan_jumlah_mahasiswa()

print("\n========== DATA KAMPUS ==========")
kampus.tampilkan_info_kampus(kampus.nama)
print("Status Nama Kampus:", "Valid" if kampus.valid else "Tidak Valid")