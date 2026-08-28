#  Kapsülleme (Encapsulation) ile Gizli Değişkenler
class Cuzdan:
    def __init__(self, baslangic_puani: int = 0):
        # '__' ile başlayan değişkenler dışarıdan doğrudan değiştirilemez (private)
        self.__puan = baslangic_puani

    def puan_ekle(self, miktar: int):
        if miktar > 0:
            self.__puan += miktar

    def puan_goster(self) -> int:
        return self.__puan