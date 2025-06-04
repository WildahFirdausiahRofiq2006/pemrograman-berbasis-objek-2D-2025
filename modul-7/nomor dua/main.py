from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def main():
    print("=== Sistem Pemesanan Kendaraan ===")

    usia_input = input("Masukkan usia Anda: ")
    if not usia_input.isdigit():
        print("Input usia harus berupa angka.")
        return
    usia = int(usia_input)

    print("\nPilih jenis kendaraan:")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")

    pilihan = input("Pilihan Anda (1/2/3): ")

    if pilihan == '1':
        kendaraan = Mobil()
    elif pilihan == '2':
        kendaraan = Motor()
    elif pilihan == '3':
        kendaraan = Sepeda()
    else:
        print("Pilihan tidak tersedia.")
        return

    kendaraan.proses_booking(usia)
    print(f"Biaya sewa: Rp {kendaraan.hitung_biaya():,.2f}")
    print(f"Informasi asuransi: {kendaraan.info_asuransi()}")

main()
