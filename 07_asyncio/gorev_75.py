class AsenkronDosya:
    async def __aenter__(self):
        return "Açık"
        
    async def __aexit__(self, exc_type, exc, tb):
        pass

async def dosya_kullan() -> str:
    async with AsenkronDosya() as durum:
        return durum