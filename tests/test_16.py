import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_16 import gitmedigi_mekanlari_bul

def test_gitmedigi_mekanlari_bul():
    tum_sistem = ["Loba Coffee", "Kütüphane", "Sinema", "Tiyatro"]
    gidilenler = ["Loba Coffee", "Sinema"]
    assert gitmedigi_mekanlari_bul(tum_sistem, gidilenler) == {"Kütüphane", "Tiyatro"}