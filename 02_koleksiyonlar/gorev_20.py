def sozluk_birlestir_topla(d1: dict, d2: dict) -> dict:
    sonuc = d1.copy()
    for k, v in d2.items():
        sonuc[k] = sonuc.get(k, 0) + v
    return sonuc