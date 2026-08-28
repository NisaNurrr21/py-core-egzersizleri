import itertools
def ureticiden_kes(uretici, baslangic: int, bitis: int) -> list:
    return list(itertools.islice(uretici, baslangic, bitis))