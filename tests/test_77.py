import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_77 import kuyruk_isleme
def test_kuyruk_isleme():
    assert asyncio.run(kuyruk_isleme()) == "Yeni Sipariş"