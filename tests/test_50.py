import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_50 import Kampanya
def test_kampanya_str():
    k = Kampanya("Yaz İndirimi", 20)
    assert str(k) == "Yaz İndirimi: %20 İndirim"