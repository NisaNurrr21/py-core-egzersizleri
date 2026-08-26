import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_17 import birlestir_ve_sirala
def test_birlestir_ve_sirala():
    assert birlestir_ve_sirala([3, 1, 2], [2, 4, 5]) == [1, 2, 3, 4, 5]