
from pathlib import Path
(str(Path(__file__).parent.parent / "03_generator_itertools"))
from gorev_30 import ikili_permutasyonlar
def test_ikili_permutasyonlar():
    # Permütasyonda sıra önemlidir, ("B", "A") da listeye dahil olur
    assert len(ikili_permutasyonlar(["A", "B", "C"])) == 6