import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_34 import tekleri_filtrele
def test_tekleri_filtrele():
    assert tekleri_filtrele([1, 2, 3, 4, 5, 6]) == [1, 3, 5]