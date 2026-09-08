
from pathlib import Path
(str(Path(__file__).parent.parent / "01_string_isleme"))
from gorev_10 import uzanti_bul
def test_uzanti_bul():
    assert uzanti_bul("vesikalik.jpg") == "jpg"
    assert uzanti_bul("gizlidosya") == ""