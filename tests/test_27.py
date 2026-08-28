import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_27 import fibonacci_uret
def test_fibonacci_uret():
    assert list(fibonacci_uret(5)) == [0, 1, 1, 2, 3]