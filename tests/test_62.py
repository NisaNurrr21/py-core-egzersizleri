import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_62 import listeyi_topla
def test_listeyi_topla():
    assert listeyi_topla([1, 2, 3]) == 6