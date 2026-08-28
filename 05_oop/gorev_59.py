#  Kendi Hata Sınıfımızı (Custom Exception) Yazma
class StokHatasi(Exception):
    pass

def stok_dus(mevcut: int, miktar: int) -> int:
    if miktar > mevcut:
        raise StokHatasi("Stok yetersiz!")
    return mevcut - miktar