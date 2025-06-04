from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def proses_booking(self, usia):
        pass

    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def info_asuransi(self):
        pass
