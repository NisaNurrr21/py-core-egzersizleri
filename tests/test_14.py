import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_14 import siparis_sayilarini_bul

def test_siparis_sayilarini_bul():
    siparisler = ["Filtre Kahve", "Çay", "Filtre Kahve", "Pasta", "Çay", "Filtre Kahve"]
    assert siparis_sayilarini_bul(siparisler) == {"Filtre Kahve": 3, "Çay": 2, "Pasta": 1}
    assert siparis_sayilarini_bul([]) == {}