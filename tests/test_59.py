
from pathlib import Path
(str(Path(__file__).parent.parent / "05_oop"))
from gorev_59 import stok_dus, StokHatasi
import pytest
def test_custom_exception():
    assert stok_dus(10, 3) == 7
    with pytest.raises(StokHatasi):
        stok_dus(5, 10)