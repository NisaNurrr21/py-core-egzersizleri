
from pathlib import Path
(str(Path(__file__).parent.parent / "05_oop"))
from gorev_54 import SMSBildirim, Bildirim
def test_abstract_class():
    sms = SMSBildirim()
    assert sms.gonder() == "SMS İletildi"