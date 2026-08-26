import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_22 import listeyi_parcala
def test_listeyi_parcala():
    assert listeyi_parcala([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [3, 4], [5, 6]]