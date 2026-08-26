def ortak_mekanlari_bul(kullanici1: list, kullanici2: list) -> set:
    # Listeleri Set'e (kümeye) çevirip intersection (kesişim) metodunu kullanıyoruz
    return set(kullanici1).intersection(set(kullanici2))