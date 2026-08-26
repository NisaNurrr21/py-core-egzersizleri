import sys
from pathlib import Path

# Python'un görev dosyamızı bulabilmesi için klasör yolunu tanıtıyoruz
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))

from gorev_01 import sesli_harfleri_kaldir

def test_sesli_harfleri_kaldir():
    assert sesli_harfleri_kaldir("Backend") == "Bcknd"
    assert sesli_harfleri_kaldir("FastAPI") == "FstP"
    assert sesli_harfleri_kaldir("Müdavim Sepeti") == "Mdvm Spt"
    assert sesli_harfleri_kaldir("aeiou") == ""