class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        self.__umur = value

    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, value):
        self.__keluhan = value

    def info(self):
        return f"Nama: {self.__nama}, Umur: {self.__umur}, Keluhan: {self.__keluhan}"

class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.__daftar_pasien.append(pasien)

    def tampilkan_semua_pasien(self):
        if not self.__daftar_pasien:
            print("Tidak ada pasien di klinik.")
        else:
            print("\nDaftar Pasien di Klinik:")
            for pasien in self.__daftar_pasien:
                print(pasien.info())


def main():
    klinik = Klinik()

    print("=====SELAMAT DATANG DI KLINIK SEHAT=====")

    while True:
        print("\nMenu Klinik:")
        print("1. Tambah Pasien")
        print("2. Lihat Daftar Pasien")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            nama = input("Nama Pasien: ")
            umur_input = input("Umur Pasien: ")
            if umur_input.isdigit():
                umur = int(umur_input)
                keluhan = input("Keluhan Pasien: ")
                pasien_baru = Pasien(nama, umur, keluhan)
                klinik.tambah_pasien(pasien_baru)
                print("Pasien berhasil ditambahkan.")
            else:
                print("Umur harus berupa angka.")
        
        elif pilihan == "2":
            klinik.tampilkan_semua_pasien()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan aplikasi klinik!")
            break

        else:
            print("Pilihan tidak valid. Ayo coba lagi.")

main()
