#  @classmethod ile Alternatif Obje Üretici
class MusteriProfili:
    def __init__(self, ad: str, yas: int):
        self.ad = ad
        self.yas = yas

    @classmethod
    def metinden_olustur(cls, veri: str):
        ad, yas = veri.split("-")
        return cls(ad, int(yas))