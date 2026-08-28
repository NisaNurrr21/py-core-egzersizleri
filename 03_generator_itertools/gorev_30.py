import itertools
def ikili_permutasyonlar(liste: list) -> list:
    return list(itertools.permutations(liste, 2))