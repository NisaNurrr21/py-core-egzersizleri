import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_42 import print_ciktisini_yakala
def test_print_ciktisini_yakala():
    def test_fonk():
        print("Backend API Calisiyor")
    assert print_ciktisini_yakala(test_fonk) == "Backend API Calisiyor"