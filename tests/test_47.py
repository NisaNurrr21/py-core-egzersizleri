import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_47 import Cuzdan
def test_cuzdan_kapsulleme():
    c = Cuzdan(100)
    c.puan_ekle(50)
    assert c.puan_goster() == 150
    # Negatif puan eklenmesini engelle
    c.puan_ekle(-20) 
    assert c.puan_goster() == 150