import asyncio

async def hata_firlat():
    raise ValueError("Bozuk Veri")

async def basarili():
    return "OK"

async def topla_ve_hata_yakala() -> list:
    # return_exceptions=True sayesinde bir hata olsa bile diğerleri iptal olmaz
    return await asyncio.gather(basarili(), hata_firlat(), return_exceptions=True)