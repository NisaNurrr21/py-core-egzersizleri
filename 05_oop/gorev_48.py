#  Kalıtım (Inheritance) ve Metot Ezme (Overriding)
class Isletme:
    def __init__(self, ad: str):
        self.ad = ad
        
    def komisyon_hesapla(self, tutar: float) -> float:
        return tutar * 0.10 # Standart %10 komisyon

class Kafe(Isletme):
    def komisyon_hesapla(self, tutar: float) -> float:
        return tutar * 0.05 # Kafeler için indirimli %5 komisyon