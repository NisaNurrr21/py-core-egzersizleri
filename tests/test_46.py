import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_46 import Musteri
def test_musteri_sinifi():
    m = Musteri("Nisa", "5551234567")
    assert m.isim == "Nisa"
    assert m.bilgileri_getir() == "Nisa - 5551234567"