class Singa:
    def __init__(self, nama, umur, suara):
        self.nama = nama
        self.umur = umur
        self.suara = suara

    def suara_singa(self):
        print(f"{self.nama} adalah singa berumur {self.umur} tahun dan suka mengaum: {self.suara}")

class Domba:
    def __init__(self, nama, umur, suara):
        self.nama = nama
        self.umur = umur
        self.suara = suara

    def suara_domba(self):
        print(f"{self.nama} adalah domba berumur {self.umur} tahun dan suka mengembik: {self.suara}")

class Gajah:
    def __init__(self, nama, umur, suara):
        self.nama = nama
        self.umur = umur
        self.suara = suara

    def suara_gajah(self):
        print(f"{self.nama} adalah gajah berumur {self.umur} tahun dan mengeluarkan suara: {self.suara}")

data_singa = [("makeu", 3, "rawrr"), ("emin", 7, "graww"), ("icung", 4, "roaarr")]
data_domba = [("shaun", 4, "mbeek"), ("the", 2, "baaa"),("sheep", 1, "mbeekk")]
data_gajah = [("mingming", 12, "prroo"), ("skups", 9, "truuu"), ("enon", 8, "brooo")]

print("=== Singa ===")
for nama, umur, suara in data_singa:
    singa = Singa(nama, umur, suara)
    singa.suara_singa()

print("\n=== Domba ===")
for nama, umur, suara in data_domba:
    domba = Domba(nama, umur, suara)
    domba.suara_domba()

print("\n=== Gajah ===")
for nama, umur, suara in data_gajah:
    gajah = Gajah(nama, umur, suara)
    gajah.suara_gajah()
