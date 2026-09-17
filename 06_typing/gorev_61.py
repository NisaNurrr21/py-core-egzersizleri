from typing import TypedDict, Literal

class Kullanici(TypedDict):
    isim: str
    yas: int
    rol: Literal["admin", "user", "guest"]

def yetki_kontrol(kullanici: Kullanici) -> bool:
    return kullanici["rol"] == "admin"

# --- Testlerin geçmesi için beklenen orijinal fonksiyon ---
def temel_tipler(a: int, b: float, c: str, d: bool) -> tuple:
    return (a, b, c, d)
