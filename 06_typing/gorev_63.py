from typing import Dict
def stok_durumu(stoklar: Dict[str, int], urun: str) -> int:
    return stoklar.get(urun, 0)