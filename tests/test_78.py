import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "07_asyncio"))
import asyncio
from gorev_78 import artir, sayac
def test_artir():
    # Sayacı sıfırla, iki işlemi aynı anda kilit yardımıyla çalıştır
    import gorev_78
    gorev_78.sayac = 0
    async def calistir():
        await asyncio.gather(artir(), artir())
    asyncio.run(calistir())
    assert gorev_78.sayac == 2