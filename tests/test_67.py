import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_67 import islem_yap
def test_islem_yap():
    assert islem_yap(10, 5, lambda x, y: x + y) == 15