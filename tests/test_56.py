import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_54 import SMSBildirim
from gorev_56 import toplu_bildirim_gonder
class EmailBildirim: # Polimorfizm için sahte sınıf
    def gonder(self): return "Email İletildi"

def test_polymorphism():
    liste = [SMSBildirim(), EmailBildirim()]
    sonuclar = toplu_bildirim_gonder(liste)
    assert sonuclar == ["SMS İletildi", "Email İletildi"]