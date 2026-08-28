import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_52 import MusteriProfili
def test_classmethod_olustur():
    m = MusteriProfili.metinden_olustur("Nisa-21")
    assert m.ad == "Nisa"
    assert m.yas == 21