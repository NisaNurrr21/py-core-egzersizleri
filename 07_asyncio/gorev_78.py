import asyncio

sayac = 0
kilit = asyncio.Lock()

async def artir():
    global sayac
    async with kilit: # Aynı anda sadece 1 işlemin buraya girmesini sağlar
        gecici = sayac
        await asyncio.sleep(0.01)
        sayac = gecici + 1