import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_80 import topla_ve_hata_yakala
def test_topla_ve_hata_yakala():
    sonuclar = asyncio.run(topla_ve_hata_yakala())
    assert sonuclar[0] == "OK"
    assert isinstance(sonuclar[1], ValueError)