from buku_fiksi import BukuFiksi
from buku_referensi import BukuReferensi

def buat_buku():
    jenis = input("Jenis buku (fiksi/referensi): ").strip().lower()
    judul = input("Judul buku: ")
    penulis = input("Penulis: ")

    if jenis == "fiksi":
        return BukuFiksi(judul, penulis)
    elif jenis == "referensi":
        return BukuReferensi(judul, penulis)
    else:
        print("Jenis buku tidak dikenali.")
        return None

def main():
    print("=== PERPUSTAKAAN TUNG TUNG SAHUR ===")
    buku = buat_buku()
    if not buku:
        return

    while True:
        print("\nMenu:")
        print("1. Info Buku")
        print("2. Pinjam Buku")
        print("3. Kembalikan Buku")
        print("4. Reservasi Buku")
        print("5. Batalkan Reservasi")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print(buku.info())
        elif pilihan == "2":
            if isinstance(buku, BukuFiksi):
                nama = input("Nama peminjam: ")
                buku.pinjam(nama)
            else:
                print("Buku ini tidak dapat dipinjam.")
        elif pilihan == "3":
            if isinstance(buku, BukuFiksi):
                buku.kembalikan()
            else:
                print("Buku ini tidak dapat dikembalikan.")
        elif pilihan == "4":
            nama = input("Nama pemesan: ")
            buku.reservasi(nama)
        elif pilihan == "5":
            buku.batalkan_reservasi()
        elif pilihan == "6":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

main()