#  @property ve @setter ile Veri Kontrolü
class Urun:
    def __init__(self, ad: str, fiyat: float):
        self.ad = ad
        self.fiyat = fiyat # Bu atama setter'ı tetikler

    @property
    def fiyat(self):
        return self._fiyat

    @fiyat.setter
    def fiyat(self, deger):
        if deger < 0:
            raise ValueError("Fiyat negatif olamaz")
        self._fiyat = deger