import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_76 import sayiciyi_kullan
def test_sayiciyi_kullan():
    assert asyncio.run(sayiciyi_kullan()) == [0, 1, 2]