class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_data(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Prodi: {self.prodi}, Alamat: {self.alamat}"

daftar_mahasiswa = []

for i in range(3):
    print(f"Masukkan data Mahasiswa {i + 1}:")
    nama = input("Nama   : ")
    nim = input("NIM    : ")
    prodi = input("Prodi  : ")
    alamat = input("Alamat : ")
    print()  

    mhs = Mahasiswa(nama, nim, prodi, alamat)
    daftar_mahasiswa.append(mhs)

print("Data Mahasiswa:")
for i in range(len(daftar_mahasiswa)):
    print(f"Mahasiswa {i + 1}: {daftar_mahasiswa[i].tampilkan_data()}")
