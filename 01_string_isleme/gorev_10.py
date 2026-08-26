def uzanti_bul(dosya_adi: str) -> str:
    if "." in dosya_adi:
        return dosya_adi.split(".")[-1]
    return ""