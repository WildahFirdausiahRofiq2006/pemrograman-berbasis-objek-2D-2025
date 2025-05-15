class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul         
        self.__penulis = penulis      
        self.__jumlah_halaman = jumlah_halaman 

    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def judul(self, value):
        self.__judul = value

    @property
    def penulis(self):
        return self.__penulis

    @penulis.setter
    def penulis(self, value):
        self.__penulis = value

    @property
    def jumlah_halaman(self):
        return self.__jumlah_halaman

    @jumlah_halaman.setter
    def jumlah_halaman(self, value):
        self.__jumlah_halaman = value

class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []  

    def tambah_buku(self, buku):
        self.__daftar_buku.append(buku)

    def tampilkan_semua_buku(self):
        if not self.__daftar_buku:
            print("Tidak ada buku di perpustakaan.")
        else:
            print("\nDaftar Buku di Perpustakaan:")
            for buku in self.__daftar_buku:
                print(f"Judul: {buku.judul}, Penulis: {buku.penulis}, Jumlah Halaman: {buku.jumlah_halaman}")

def main():
    perpustakaan = Perpustakaan()

    print("=====SELAMAT DATANG DI PERPUSTAKAAN NCT DREAM=====")

    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            judul = input("Judul Buku: ")
            penulis = input("Penulis Buku: ")
            jumlah_halaman_input = input("Jumlah Halaman: ")
            if jumlah_halaman_input.isdigit():
                jumlah_halaman = int(jumlah_halaman_input)
                buku_baru = Buku(judul, penulis, jumlah_halaman)
                perpustakaan.tambah_buku(buku_baru)
                print("Buku berhasil ditambahkan.")
            else:
                print("Jumlah halaman harus berupa angka.")
        
        elif pilihan == "2":
            perpustakaan.tampilkan_semua_buku()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan aplikasi perpustakaan;)")
            break

        else:
            print("Pilihan tidak valid. Ayo coba lagi!")

main()
