from abc import ABC, abstractmethod

class MetodePembayaran(ABC):
    @abstractmethod
    def hitung_total(self, jumlah):
        pass

    @abstractmethod
    def bayar(self, jumlah):
        pass
