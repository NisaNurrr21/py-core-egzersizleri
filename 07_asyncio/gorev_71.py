import asyncio

async def asenkron_mesaj() -> str:
    await asyncio.sleep(0.1) # İşlemi bloke etmeden bekler
    return "Asenkron Tamamlandi"