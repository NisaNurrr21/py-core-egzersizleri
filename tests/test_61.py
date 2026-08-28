import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "06_typing"))
from gorev_61 import temel_tipler
def test_temel_tipler():
    assert temel_tipler("Ali", 25) == "Ali 25 yaşında"