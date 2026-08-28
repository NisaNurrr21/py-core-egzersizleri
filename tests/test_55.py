import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_55 import SatisBelgesi
def test_coklu_kalitim():
    belge = SatisBelgesi()
    assert belge.rapor_uret() == "Rapor Hazır"
    assert belge.yazdir() == "Yazıcıya Gönderildi"