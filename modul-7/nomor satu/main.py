from pembayaran_tunai import PembayaranTunai
from pembayaran_kartu_kredit import PembayaranKartuKredit
from pembayaran_dompet_digital import PembayaranDompetDigital

def main():
    print("=== Sistem Pembayaran ===")

    jumlah_input = input("Masukkan jumlah pembayaran (Rp): ")
    if not jumlah_input.isdigit():
        print("Input tidak valid. Harus berupa angka bulat.")
        return
    jumlah = float(jumlah_input)

    print("\nPilih metode pembayaran:")
    print("1. Tunai")
    print("2. Kartu Kredit")
    print("3. Dompet Digital")

    pilihan = input("Masukkan pilihan Anda (1/2/3): ")
    if pilihan not in ('1', '2', '3'):
        print("Pilihan tidak tersedia.")
        return

    if pilihan == '1':
        metode = PembayaranTunai()
    elif pilihan == '2':
        metode = PembayaranKartuKredit()
    else:
        metode = PembayaranDompetDigital()

    metode.bayar(jumlah)

main()
