import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_63 import stok_durumu
def test_stok_durumu():
    assert stok_durumu({"Kahve": 10}, "Kahve") == 10
    assert stok_durumu({"Kahve": 10}, "Çay") == 0