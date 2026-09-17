from typing import TypeVar, List, Dict

# T adında esnek bir tip değişkeni oluşturuyoruz
T = TypeVar('T')

def ilk_elemani_getir(liste: List[T]) -> T:
    if not liste:
        raise ValueError("Liste boş olamaz")
    return liste[0]

# --- Testlerin geçmesi için beklenen orijinal fonksiyon ---
def stok_durumu(stok: Dict[str, int], urun: str) -> int:
    return stok.get(urun, 0)
