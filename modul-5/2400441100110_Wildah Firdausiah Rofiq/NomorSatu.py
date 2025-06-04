from abc import ABC, abstractmethod

class Manusia(ABC):

    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def makan(self):
        pass

class Joko(Manusia):
    def berbicara(self):
        print("Joko berbicara dengan suara lantang dan percaya diri.")

    def bekerja(self):
        print("Joko bekerja sebagai insinyur di proyek besar.")

    def makan(self):
        print("Joko makan dengan cepat karena sibuk.")

class Beni(Manusia):
    def berbicara(self):
        print("Beni berbicara dengan tenang dan hati-hati.")

    def bekerja(self):
        print("Beni bekerja sebagai guru di sekolah dasar.")    

    def makan(self):
        print("Beni makan dengan perlahan sambil membaca buku.")

class Fani(Manusia):
    def berbicara(self):
        print("Fani berbicara dengan ceria dan penuh semangat.")

    def bekerja(self):
        print("Fani bekerja sebagai desainer grafis kreatif.")

    def makan(self):
        print("Fani makan sambil mencoba makanan baru dari berbagai negara.")

class Jani(Manusia):
    def berbicara(self):
        print("Jani berbicara dengan suara lembut dan sopan.")

    def bekerja(self):
        print("Jani bekerja dari rumah sebagai penulis konten.")

    def makan(self):
        print("Jani makan makanan sehat dan organik setiap hari.")

karakter_dict = {
    "joko": Joko,
    "beni": Beni,
    "fani": Fani,
    "jani": Jani
}

def main():
    print("Karakter yang tersedia: Joko, Beni, Fani, Jani")
    print("Ketik 'keluar' untuk menghentikan program.")
    while True:
        nama = input("Masukkan nama karakter yang ingin dilihat: ").lower()

        if nama == "keluar":
            print("Program dihentikan.")
            break

        karakter = karakter_dict.get(nama)
        if karakter:
            objek = karakter()
            objek.berbicara()
            objek.bekerja()
            objek.makan()
            print("-" * 45)
        else:
            print("Karakter tidak ditemukan. Coba lagi.")

main()