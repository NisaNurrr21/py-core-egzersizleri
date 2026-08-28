import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_32 import ureticiden_kes
def test_ureticiden_kes():
    uretici = (x for x in range(10)) # 0'dan 9'a sayılar
    assert ureticiden_kes(uretici, 2, 5) == [2, 3, 4]