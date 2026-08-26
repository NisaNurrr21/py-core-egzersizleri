import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))
from gorev_03 import palindrom_mu

def test_palindrom_mu():
    assert palindrom_mu("Kavak") == True
    assert palindrom_mu("Backend") == False
    assert palindrom_mu("Radar") == True