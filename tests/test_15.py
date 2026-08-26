import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_15 import en_cok_harcayanlari_sirala

def test_en_cok_harcayanlari_sirala():
    musteriler = [("Taha", 150), ("Sümeyra", 300), ("Şevin", 120)]
    beklenen = [("Sümeyra", 300), ("Taha", 150), ("Şevin", 120)]
    assert en_cok_harcayanlari_sirala(musteriler) == beklenen