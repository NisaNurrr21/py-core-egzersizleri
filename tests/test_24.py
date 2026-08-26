import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_24 import harf_frekansi
def test_harf_frekansi():
    frekans = harf_frekansi("nisa")
    assert frekans["n"] == 1 and frekans["a"] == 1