def gitmedigi_mekanlari_bul(tum_mekanlar: list, gidilen_mekanlar: list) -> set:
    # '-' operatörü iki küme (set) arasındaki farkı alır (Birinci kümede olup ikincide olmayanlar)
    return set(tum_mekanlar) - set(gidilen_mekanlar)