import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_70 import ilk_elemani_getir
def test_ilk_elemani_getir():
    assert ilk_elemani_getir([1, 2, 3]) == 1
    assert ilk_elemani_getir(["a", "b"]) == "a"