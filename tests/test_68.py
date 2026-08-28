import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_68 import her_seyi_kabul_et
def test_her_seyi_kabul_et():
    assert her_seyi_kabul_et(123) == "123"
    assert her_seyi_kabul_et([1, 2]) == "[1, 2]"