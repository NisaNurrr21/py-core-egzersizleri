import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "05_oop"))
from gorev_53 import Dogrulama
def test_staticmethod():
    assert Dogrulama.tc_gecerli_mi("12345678901") == True
    assert Dogrulama.tc_gecerli_mi("1234A678901") == False