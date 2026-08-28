# Sihirli Metot (Magic Method) ile Operatör Aşırı Yükleme (__add__)
class SadakatPuani:
    def __init__(self, miktar: int):
        self.miktar = miktar

    def __add__(self, diger):
        return SadakatPuani(self.miktar + diger.miktar)