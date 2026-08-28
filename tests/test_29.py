import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_29 import ikili_kombinasyonlar
def test_ikili_kombinasyonlar():
    assert ikili_kombinasyonlar(["A", "B", "C"]) == [("A", "B"), ("A", "C"), ("B", "C")]