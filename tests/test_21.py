import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_21 import ortak_anahtarlar
def test_ortak_anahtarlar():
    assert ortak_anahtarlar({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"b"}