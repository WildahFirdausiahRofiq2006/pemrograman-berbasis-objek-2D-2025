import math

class BangunDatar:
    def luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun_datar):
    print(f"Luas: {bangun_datar.luas():.2f}\n")

def main():
    while True:
        print("=== Program Hitung Luas Bangun Datar ===")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("4. Keluar")
        
        pilihan = input("Pilih bangun datar (1/2/3/4): ")

        if pilihan == "1":
            sisi = float(input("Masukkan panjang sisi: "))
            bangun = Persegi(sisi)
            cetak_luas(bangun)
        elif pilihan == "2":
            jari_jari = float(input("Masukkan jari-jari: "))
            bangun = Lingkaran(jari_jari)
            cetak_luas(bangun)
        elif pilihan == "3":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            bangun = Segitiga(alas, tinggi)
            cetak_luas(bangun)
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

main()