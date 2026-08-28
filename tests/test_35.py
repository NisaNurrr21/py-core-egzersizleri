import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_35 import kareleri_uret
def test_kareleri_uret():
    gen = kareleri_uret([1, 2, 3])
    import types
    assert isinstance(gen, types.GeneratorType) # Dönen değerin liste değil generator olduğunu test ederiz
    assert list(gen) == [1, 4, 9]