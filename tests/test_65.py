import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_65 import kullanici_bul
def test_kullanici_bul():
    assert kullanici_bul(1) == "Nisa"
    assert kullanici_bul(99) is None