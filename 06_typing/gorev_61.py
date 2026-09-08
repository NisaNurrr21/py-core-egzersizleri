from typing import TypedDict, Literal

class Kullanici(TypedDict):
    isim: str
    yas: int
    rol: Literal["admin", "user", "guest"]

def yetki_kontrol(kullanici: Kullanici) -> bool:
    return kullanici["rol"] == "admin"