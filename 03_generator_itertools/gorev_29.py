import itertools
def ikili_kombinasyonlar(liste: list) -> list:
    return list(itertools.combinations(liste, 2))