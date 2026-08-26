import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))

from gorev_13 import ortak_mekanlari_bul

def test_ortak_mekanlari_bul():
    k1 = ["Loba Coffee", "Kutuphane", "Sinema"]
    k2 = ["Sinema", "Loba Coffee", "Spor Salonu"]
    assert ortak_mekanlari_bul(k1, k2) == {"Loba Coffee", "Sinema"}