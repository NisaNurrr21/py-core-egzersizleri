from typing import Protocol

class Loglayici(Protocol):
    def log_yaz(self, mesaj: str) -> None: ...

class DosyaLoglayici:
    def log_yaz(self, mesaj: str) -> None:
        print(f"Dosyaya yazıldı: {mesaj}")

def islem_yap(log_sistemi: Loglayici) -> None:
    log_sistemi.log_yaz("Sistem başarıyla başlatıldı")