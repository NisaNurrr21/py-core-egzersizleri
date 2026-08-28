import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_44 import MockVeritabani
def test_mock_veritabani():
    db = MockVeritabani()
    assert db.bagli_mi is False
    with db as baglanti:
        assert baglanti.bagli_mi is True
    assert db.bagli_mi is False