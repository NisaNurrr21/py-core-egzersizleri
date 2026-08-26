def ortak_anahtarlar(d1: dict, d2: dict) -> set:
    return set(d1.keys()) & set(d2.keys())