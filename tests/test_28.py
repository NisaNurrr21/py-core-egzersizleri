import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_28 import listeleri_zincirle
def test_listeleri_zincirle():
    assert listeleri_zincirle([1, 2], [3, 4]) == [1, 2, 3, 4]