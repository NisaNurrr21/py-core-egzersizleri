import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))
from gorev_09 import bosluklari_temizle
def test_bosluklari_temizle():
    assert bosluklari_temizle("  Çok   fazla   boşluk  var  ") == "Çok fazla boşluk var"