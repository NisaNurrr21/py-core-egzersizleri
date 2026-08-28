import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_79 import is_parcaciginda_calistir
def test_is_parcaciginda_calistir():
    assert asyncio.run(is_parcaciginda_calistir()) == "Senkron"