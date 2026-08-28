#Sınıf (Class) ve Nesne (Object) Temelleri
class Musteri:
    def __init__(self, isim: str, telefon: str):
        self.isim = isim
        self.telefon = telefon

    def bilgileri_getir(self) -> str:
        return f"{self.isim} - {self.telefon}"