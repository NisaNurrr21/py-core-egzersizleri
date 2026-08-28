import asyncio

async def islem(id: int) -> int:
    await asyncio.sleep(0.1)
    return id * 2

async def coklu_islem() -> list:
    # İki işlemi aynı anda başlatır ve sonuçlarını liste olarak döner
    return await asyncio.gather(islem(1), islem(2))