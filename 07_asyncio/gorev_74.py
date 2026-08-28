import asyncio

async def yavas_islem() -> str:
    await asyncio.sleep(1.0)
    return "Başarılı"

async def zaman_asinimi_kontrolu() -> str:
    try:
        # Fonksiyonun 0.1 saniyede bitmesini bekler, bitmezse hata fırlatır
        return await asyncio.wait_for(yavas_islem(), timeout=0.1)
    except asyncio.TimeoutError:
        return "Zaman Aşımı"