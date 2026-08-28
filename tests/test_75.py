import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_75 import dosya_kullan
def test_dosya_kullan():
    assert asyncio.run(dosya_kullan()) == "Açık"