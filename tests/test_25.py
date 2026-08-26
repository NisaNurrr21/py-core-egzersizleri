import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "02_koleksiyonlar"))
from gorev_25 import sadece_benzersizler
def test_sadece_benzersizler():
    assert sadece_benzersizler([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]