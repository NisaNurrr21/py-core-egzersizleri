import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_51 import Urun
import pytest
def test_urun_fiyat_kontrol():
    u = Urun("Kahve", 50)
    assert u.fiyat == 50
    with pytest.raises(ValueError):
        u.fiyat = -10