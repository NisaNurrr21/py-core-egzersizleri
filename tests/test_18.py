import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_18 import sozlugu_tersine_cevir
def test_sozlugu_tersine_cevir():
    assert sozlugu_tersine_cevir({"Taha": "Backend", "Sümeyra": "Frontend"}) == {"Backend": "Taha", "Frontend": "Sümeyra"}