import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_48 import Isletme, Kafe
def test_isletme_kalitim():
    standart_isletme = Isletme("Butik")
    kafe_isletmesi = Kafe("Loba Coffee")
    
    assert standart_isletme.komisyon_hesapla(100) == 10.0
    assert kafe_isletmesi.komisyon_hesapla(100) == 5.0