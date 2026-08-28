import asyncio
import time

def bloklayan_islem() -> str:
    time.sleep(0.1)
    return "Senkron"

async def is_parcaciginda_calistir() -> str:
    return await asyncio.to_thread(bloklayan_islem)