def sesli_harfleri_kaldir(metin: str) -> str:
    """
    Gelen metindeki tüm sesli harfleri (a, e, ı, i, o, ö, u, ü) 
    büyük/küçük harf fark etmeksizin siler ve kalan karakterleri döndürür.
    """
    # Sesli harflerin hem küçük hem büyük hallerini bir değişkende tutuyoruz
    sesliler = "aeıioöuüAEIİOÖUÜ"
    
    # List Comprehension ve join kullanarak metni temizliyoruz
    temiz_metin = "".join([harf for harf in metin if harf not in sesliler])
    
    return temiz_metin