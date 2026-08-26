def toplam_puan(puan_gecmisi: dict) -> int:
    # values() metodu sözlükteki sadece sayıları (değerleri) alır, sum() toplar
    return sum(puan_gecmisi.values())