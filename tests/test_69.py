import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_69 import verileri_isle
def test_verileri_isle():
    assert verileri_isle({"puanlar": [10, 20, 30]}) == 60