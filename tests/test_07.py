import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))
from gorev_07 import kelime_say
def test_kelime_say():
    assert kelime_say("Backend harika bir alan") == 4
    assert kelime_say("   TekKelime   ") == 1
