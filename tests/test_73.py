import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_73 import gorev_zamanla
def test_gorev_zamanla():
    assert asyncio.run(gorev_zamanla()) == "Görev Bitti"