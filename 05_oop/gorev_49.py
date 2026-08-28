#  Sınıf Değişkeni (Class Variable) Kullanımı
class SistemKullanicisi:
    # Bu değişken tekil bir nesneye değil, tüm sınıfa aittir
    aktif_kullanici_sayisi = 0

    def __init__(self, kullanici_adi: str):
        self.kullanici_adi = kullanici_adi
        SistemKullanicisi.aktif_kullanici_sayisi += 1

    def cikis_yap(self):
        SistemKullanicisi.aktif_kullanici_sayisi -= 1