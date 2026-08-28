from typing import Optional
def kullanici_bul(kullanici_id: int) -> Optional[str]:
    kullanicilar = {1: "Nisa", 2: "Taha"}
    return kullanicilar.get(kullanici_id) # Bulamazsa otomatik None döner