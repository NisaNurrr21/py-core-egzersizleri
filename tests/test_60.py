
from pathlib import Path
(str(Path(__file__).parent.parent / "05_oop"))
from gorev_60 import KampanyaKodu
def test_dataclass():
    k = KampanyaKodu("YAZ2026", 15.0)
    assert k.kod == "YAZ2026"
    assert k.aktif_mi == True