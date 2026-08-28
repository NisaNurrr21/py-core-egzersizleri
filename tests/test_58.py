import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_58 import SadakatPuani
def test_operator_overloading():
    p1 = SadakatPuani(100)
    p2 = SadakatPuani(50)
    toplam = p1 + p2
    assert toplam.miktar == 150