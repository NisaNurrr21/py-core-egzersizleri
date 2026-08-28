import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_31 import kartezyen_carpim
def test_kartezyen_carpim():
    assert kartezyen_carpim([1, 2], ["A", "B"]) == [(1, "A"), (1, "B"), (2, "A"), (2, "B")]