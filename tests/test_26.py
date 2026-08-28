import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_26 import sayici
def test_sayici():
    gen = sayici(3)
    assert next(gen) == 1
    assert list(gen) == [2, 3] # Geriye kalanları listeler