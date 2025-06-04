from abc import ABC, abstractmethod

class Reservasi(ABC):
    @abstractmethod
    def reservasi(self, nama_pemesan):
        pass

    @abstractmethod
    def batalkan_reservasi(self):
        pass
