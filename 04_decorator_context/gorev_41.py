from contextlib import contextmanager

@contextmanager
def gecici_ayar(ayarlar: dict, anahtar: str, gecici_deger):
    """Bir sözlükteki değeri geçici olarak değiştirir, with bloğu bitince eski haline getirir."""
    eski_deger = ayarlar.get(anahtar)
    ayarlar[anahtar] = gecici_deger
    try:
        yield
    finally:
        if eski_deger is None:
            del ayarlar[anahtar]
        else:
            ayarlar[anahtar] = eski_deger