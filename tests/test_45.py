import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
import os
from gorev_45 import gecici_dizin
def test_gecici_dizin(tmp_path):
    baslangic_dizini = os.getcwd()
    with gecici_dizin(str(tmp_path)):
        assert os.getcwd() == str(tmp_path)
    assert os.getcwd() == baslangic_dizini