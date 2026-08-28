import asyncio

async def asenkron_sayici(sinir: int):
    for i in range(sinir):
        await asyncio.sleep(0.01)
        yield i

async def sayiciyi_kullan() -> list:
    return [x async for x in asenkron_sayici(3)]