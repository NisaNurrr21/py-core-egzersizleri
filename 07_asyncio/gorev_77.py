import asyncio

async def kuyruk_isleme() -> str:
    kuyruk = asyncio.Queue()
    await kuyruk.put("Yeni Sipariş")
    return await kuyruk.get()