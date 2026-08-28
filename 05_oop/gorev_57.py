#  Kompozisyon (Composition) - Objeleri İç İçe Kullanma
class SepetKalemi:
    def __init__(self, urun_adi: str, adet: int):
        self.urun_adi = urun_adi
        self.adet = adet

class Sepet:
    def __init__(self):
        self.icerik = []
        
    def urun_ekle(self, kalem: SepetKalemi):
        self.icerik.append(kalem)
        
    def toplam_adet(self) -> int:
        return sum(k.adet for k in self.icerik)