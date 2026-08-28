import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_66 import indirim_uygula
def test_indirim_uygula():
    assert indirim_uygula(100) == 90.0
    assert indirim_uygula(50.5) == 45.45