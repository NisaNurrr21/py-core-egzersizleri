import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))
from gorev_08 import baslik_yap
def test_baslik_yap():
    assert baslik_yap("python programlama dili") == "Python Programlama Dili"