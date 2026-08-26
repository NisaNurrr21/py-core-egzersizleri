import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_19 import min_max_bul
def test_min_max_bul():
    assert min_max_bul([10, 5, 20, 2]) == (2, 20)
    assert min_max_bul([]) == (0, 0)