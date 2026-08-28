from typing import Dict, List
KullaniciVerisi = Dict[str, List[int]]

def verileri_isle(veri: KullaniciVerisi) -> int:
    return sum(veri.get("puanlar", []))