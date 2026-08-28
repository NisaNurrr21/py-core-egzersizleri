import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_71 import asenkron_mesaj
def test_asenkron_mesaj():
    assert asyncio.run(asenkron_mesaj()) == "Asenkron Tamamlandi"