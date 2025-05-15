class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self.no_rek = no_rek
        self.nama_pemilik = nama_pemilik
        self.__saldo = saldo 

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if value >= 0:
            self.__saldo = value
        else:
            print("Saldo tidak boleh kurang dari 0")

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
        else:
            print("Jumlah setoran harus lebih besar dari 0")

    def tarik(self, jumlah):
        if jumlah > 0 and self.saldo >= jumlah:
            self.saldo -= jumlah
        else:
            print("Jumlah penarikan tidak valid atau saldo tidak cukup")

class Bank:
    def __init__(self):
        self.rekening_list = []  

    def tambah_rekening(self, no_rek, nama_pemilik, saldo_awal=0):
        rekening = RekeningBank(no_rek, nama_pemilik, saldo_awal)
        self.rekening_list.append(rekening)

    def cari_rekening(self, no_rek):
        for rekening in self.rekening_list:
            if rekening.no_rek == no_rek:
                return rekening
        return None

    def tampilkan_semua_rekening(self):
        if not self.rekening_list:
            print("Tidak ada rekening untuk ditampilkan.")
        else:
            for rekening in self.rekening_list:
                print(f"Nomor Rekening: {rekening.no_rek}, Pemilik: {rekening.nama_pemilik}, Saldo: {rekening.saldo}")


def main():
    bank = Bank()

    print("=====SELAMAT DATANG DI BANK ENHA=====")

    while True:
        print("Menu Bank:")
        print("1. Tambah Rekening Baru")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            no_rek = input("Nomor rekening: ")
            nama_pemilik = input("Nama pemilik rekening: ")
            bank.tambah_rekening(no_rek, nama_pemilik)
            print(f"Rekening {no_rek} berhasil ditambahkan dengan saldo awal 0!")

        elif pilihan == "2":
            no_rek = input("Nomor rekening : ")
            rekening = bank.cari_rekening(no_rek)
            if rekening:
                jumlah_setor = int(input("Jumlah setoran: "))
                rekening.setor(jumlah_setor)
                print(f"Setoran berhasil! Saldo baru: {rekening.saldo}")
            else:
                print("Rekening tidak ditemukan!")

        elif pilihan == "3":
            no_rek = input("Nomor rekening: ")
            rekening = bank.cari_rekening(no_rek)
            if rekening:
                jumlah_tarik = int(input("Jumlah penarikan: "))
                rekening.tarik(jumlah_tarik)
                print(f"Penarikan berhasil! Sisa saldo: {rekening.saldo}")
            else:
                print("Rekening tidak ditemukan!")

        elif pilihan == "4":
            bank.tampilkan_semua_rekening()

        elif pilihan == "5":
            print("Terima kasih telah menggunakan layanan bank;)")
            break

        else:
            print("Pilihan tidak valid. Ayo pilih lagi!!!")

main()
