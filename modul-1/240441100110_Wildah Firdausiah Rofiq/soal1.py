class Manusia:
    def __init__(self, nama, umur, alamat):  # perbaikan di sini
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        return f"{self.nama} sedang berjalan."

    def berlari(self):
        return f"{self.nama} sedang berlari."

    # method untuk menampilkan umur dan alamat
    def tampilkan_umur_dan_alamat(self):
        return f"Umur {self.nama}: {self.umur} tahun, Alamat: {self.alamat}"

# membuat objeknya
manusia1 = Manusia("firda", 19, "gresik")
manusia2 = Manusia("jay", 23, "surabaya")
manusia3 = Manusia("choi san", 25, "lampung")
manusia4 = Manusia("song mingi", 27, "danten")
manusia5 = Manusia("mark", 26, "kedamean")

# outputnya
print(manusia1.berjalan())
print(manusia1.tampilkan_umur_dan_alamat())

print(manusia2.berlari())
print(manusia2.tampilkan_umur_dan_alamat())

print(manusia3.berjalan())
print(manusia3.tampilkan_umur_dan_alamat())

print(manusia4.berlari())
print(manusia4.tampilkan_umur_dan_alamat())

print(manusia5.berjalan())
print(manusia5.tampilkan_umur_dan_alamat())
