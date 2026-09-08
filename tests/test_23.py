
from pathlib import Path
(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_23 import duzlestir
def test_duzlestir():
    assert duzlestir([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]