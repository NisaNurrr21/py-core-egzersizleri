import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_74 import zaman_asinimi_kontrolu
def test_zaman_asinimi_kontrolu():
    assert asyncio.run(zaman_asinimi_kontrolu()) == "Zaman Aşımı"