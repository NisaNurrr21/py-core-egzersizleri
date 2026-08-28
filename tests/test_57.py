import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_57 import Sepet, SepetKalemi
def test_kompozisyon():
    sepet = Sepet()
    sepet.urun_ekle(SepetKalemi("Filtre Kahve", 2))
    sepet.urun_ekle(SepetKalemi("Tatlı", 1))
    assert sepet.toplam_adet() == 3