from typing import Protocol, List

class Loglayici(Protocol):
    def log_yaz(self, mesaj: str) -> None: ...

class DosyaLoglayici:
    def log_yaz(self, mesaj: str) -> None:
        print(f"Dosyaya yazıldı: {mesaj}")

def islem_yap(log_sistemi: Loglayici) -> None:
    log_sistemi.log_yaz("Sistem başarıyla başlatıldı")

# --- Testlerin geçmesi için beklenen orijinal fonksiyon ---
def listeyi_topla(sayilar: List[int]) -> int:
    return sum(sayilar)
