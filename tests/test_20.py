import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_20 import sozluk_birlestir_topla
def test_sozluk_birlestir_topla():
    assert sozluk_birlestir_topla({"a": 10, "b": 20}, {"b": 5, "c": 30}) == {"a": 10, "b": 25, "c": 30}