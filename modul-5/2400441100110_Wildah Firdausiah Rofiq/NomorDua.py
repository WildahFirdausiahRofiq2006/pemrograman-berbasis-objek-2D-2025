from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100

    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def status(self):
        print(f"\nTipe perangkat: {self.__class__.__name__}")
        print(f"Energi tersisa: {self.energi_tersisa}%")
        print("-" * 30)

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        print(f"Laptop digunakan selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai laptop habis!")

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        print(f"Kulkas beroperasi selama {jam} jam.")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")

def main():
    print("=== Perangkat Elektronik ===")
    laptop = Laptop()
    laptop.nyalakan()
    jam_laptop = int(input("Masukkan jam penggunaan Laptop: "))
    laptop.gunakan(jam_laptop)
    laptop.status()
    laptop.matikan()

    print("\n")

    kulkas = Kulkas()
    kulkas.nyalakan()
    jam_kulkas = int(input("Masukkan jam penggunaan Kulkas: "))
    kulkas.gunakan(jam_kulkas)
    kulkas.status()
    kulkas.matikan()


main()
