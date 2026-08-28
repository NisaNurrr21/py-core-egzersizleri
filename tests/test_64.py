import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_64 import koordinat_getir
def test_koordinat_getir():
    assert koordinat_getir() == (41.0, 28.9, "İstanbul")