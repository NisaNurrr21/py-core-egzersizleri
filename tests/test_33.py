import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_33 import donguden_eleman_al
def test_donguden_eleman_al():
    assert donguden_eleman_al(["X", "Y"], 5) == ["X", "Y", "X", "Y", "X"]