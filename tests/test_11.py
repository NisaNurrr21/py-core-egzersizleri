import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))

from gorev_11 import numara_tekillestir

def test_numara_tekillestir():
    assert numara_tekillestir(["555", "532", "555", "505"]) == ["555", "532", "505"]
    assert numara_tekillestir([]) == []