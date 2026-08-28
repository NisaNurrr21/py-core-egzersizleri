import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_49 import SistemKullanicisi
def test_sinif_degiskeni():
    SistemKullanicisi.aktif_kullanici_sayisi = 0 # Testi sıfırla
    k1 = SistemKullanicisi("taha_dev")
    k2 = SistemKullanicisi("sumeyra_ui")
    
    assert SistemKullanicisi.aktif_kullanici_sayisi == 2
    k1.cikis_yap()
    assert SistemKullanicisi.aktif_kullanici_sayisi == 1