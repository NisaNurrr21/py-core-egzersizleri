import itertools
def tekleri_filtrele(sayilar: list) -> list:
    # lambda x: x % 2 == 0 şartı "çift sayılar" demektir. filterfalse çift olmayanları (tekleri) bırakır.
    return list(itertools.filterfalse(lambda x: x % 2 == 0, sayilar))