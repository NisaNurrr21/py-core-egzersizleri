import itertools
def listeleri_zincirle(liste1: list, liste2: list) -> list:
    return list(itertools.chain(liste1, liste2))