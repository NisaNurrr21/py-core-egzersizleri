import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))

from gorev_12 import toplam_puan

def test_toplam_puan():
    gecmis = {"Loba Coffee": 150, "Berber": 40, "Butik": 210}
    assert toplam_puan(gecmis) == 400
    assert toplam_puan({}) == 0