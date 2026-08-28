# Sihirli Metotlar (Magic Methods: __str__)
class Kampanya:
    def __init__(self, baslik: str, indirim_orani: int):
        self.baslik = baslik
        self.indirim_orani = indirim_orani

    def __str__(self):
        # Obje print() edildiğinde bellekteki yeri yerine bu okunabilir metni döndürür
        return f"{self.baslik}: %{self.indirim_orani} İndirim"