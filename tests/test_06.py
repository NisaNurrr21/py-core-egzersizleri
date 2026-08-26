import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))

# Sonrası senin yazdığın gibi kalacak:
from gorev_06 import anagram_mi

def test_anagram_mi():
    assert anagram_mi("listen", "silent") == True
    assert anagram_mi("elazig", "gazi") == False