
from pathlib import Path
(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_72 import coklu_islem
def test_coklu_islem():
    assert asyncio.run(coklu_islem()) == [2, 4]