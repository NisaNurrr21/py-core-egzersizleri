def siparis_sayilarini_bul(siparis_listesi: list) -> dict:
    sonuclar = {}
    for urun in siparis_listesi:
        if urun in sonuclar:
            sonuclar[urun] += 1
        else:
            sonuclar[urun] = 1
    return sonuclar