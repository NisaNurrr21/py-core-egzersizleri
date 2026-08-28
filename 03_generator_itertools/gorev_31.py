import itertools
def kartezyen_carpim(liste1: list, liste2: list) -> list:
    return list(itertools.product(liste1, liste2))