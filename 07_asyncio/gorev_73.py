import asyncio

async def arka_plan_isi() -> str:
    await asyncio.sleep(0.1)
    return "Görev Bitti"

async def gorev_zamanla() -> str:
    gorev = asyncio.create_task(arka_plan_isi())
    return await gorev